from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Slot, QFile, Qt, QTextStream

import pandas as pd

from windows.file_explorer_window import FileExplorerWindow
from widgets.file_explorer_widget import FileExplorerWidget
from adapters.TableModel import TableModel


class MainWindow(QMainWindow):

    # ------------------------------------------------------------------
    #                               INIT
    # ------------------------------------------------------------------

    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("Distribution Tool")
        self.main_widget = widget
        self.setCentralWidget(self.main_widget)

        # Signals
        self.main_widget.fileExplorerWindowRequested.connect(self.open_file_explorer_window)
        
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Archivo")
        self.help_menu = self.menu.addMenu("Ayuda")

        # ------------------------------------------------------------------
        #                            FILE MENU
        # ------------------------------------------------------------------

        # Exit QAction
        exit_action = self.file_menu.addAction("Salir", self.close)
        exit_action.setShortcut("Ctrl+Q")

        # Load QAction (First Excel)
        self.file_menu.addAction("Cargar 1er Excel", lambda: self.load_action(self.first_excel))

        # Load QAction (Second Excel)
        self.file_menu.addAction("Cargar 2do Excel", lambda: self.load_action(self.second_excel))

        # ------------------------------------------------------------------
        #                            HELP MENU
        # ------------------------------------------------------------------

        # Help QAction
        help_action = self.help_menu.addAction("Ayuda", self.help_action)
        help_action.setShortcut("Ctrl+H")


    # ------------------------------------------------------------------
    #                              SLOTS
    # ------------------------------------------------------------------

    @Slot()
    def open_file_explorer_window(self, button: int):
        if button == 1 or button == 2:
            self._insert_buttons_logic(button=button)

        if button == 3:
            self._confirm_button_logic()
            
        if button == 4:
            self._cancel_button_logic()
            
    
    @Slot()
    def help_action(self):
        QMessageBox.about(self, "Ayuda", "Esta aplicación toma como input: xxx, y devuelve" \
        "las distribuciones de cada pozo.")

    # NOT QUITE THE RIGHT APPLICATION, BUT GOOD FOR TESTING FOR NOW
    @Slot()
    def load_action(self, file_name):
        file = QFile(file_name)

        if not file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            reason = file.errorString()
            QMessageBox.warning(self, "Application", f"Cannot read file {file_name}:\n{reason}.")
            return

        info = QTextStream(file)
        with QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor):
            print(info.readAll())

    # ------------------------------------------------------------------
    #                        INTERNAL FUNCTIONS
    # ------------------------------------------------------------------

    def _load_first_excel(self, file_name):
        try:
            # Create dataframe
            df = pd.read_excel(file_name)

            # Identify unique wells
            unique_wells = df["IDENTIFICADOR"].unique()

            # Sort each well using the TOPE [m MD] column
            list_of_dfs = [df]
            list_of_dfs_1 = [group for df in list_of_dfs for _, group in df.groupby('IDENTIFICADOR')]
            # list_of_dfs_2 = [group for df in list_of_dfs_1 for _, group in df.groupby('FECHA')]
            # list_of_dfs_3 = [group for df in list_of_dfs_2 for _, group in df.groupby('CAPA')]
            final_sorted_list = [df.sort_values(by='TOPE [m MD]') for df in list_of_dfs_1]

            return unique_wells, final_sorted_list
        
        except FileNotFoundError or ValueError:
            return

    def _load_second_excel(self, file_name):
        try:
            return pd.read_excel(file_name)
        
        except FileNotFoundError or ValueError:
            return

    def _load_table(self, data):
        data_model = TableModel(data)
        self.main_widget.table.setModel(data_model)

    def _reset_button(self, button):
        if button == 1:
            del self.first_excel_dfs
            self.main_widget.insert_button_1.setEnabled(True)
        elif button == 2:
            del self.second_excel_dfs
            self.main_widget.insert_button_2.setEnabled(True)
        self.main_widget.table.hide()

    def _insert_buttons_logic(self, button):
        self.file_explorer_widget = FileExplorerWidget()
        self.file_explorer_window = FileExplorerWindow(self.file_explorer_widget)
        self.file_explorer_window.show()

        file_name = self.file_explorer_widget.file_name

        if self.file_explorer_widget.excelFileSelected:
            # Hide the file explorer
            self.file_explorer_window.hide()

            # If a file was selected from insert_button_1
            if file_name != "" and button == 1:
                self.main_widget.insert_button_1.setEnabled(False)
                (self.unique_wells, self.first_excel_dfs) = self._load_first_excel(file_name)
                
            # If a file was selected from insert_button_2
            elif file_name != "" and button == 2:
                self.main_widget.insert_button_2.setEnabled(False)
                self.second_excel_dfs = self._load_second_excel(file_name)

    def _confirm_button_logic(self):
        try:
            if len(self.first_excel_dfs) > 0 and len(self.second_excel_dfs) > 0:
                # Table only appears if the excels have already been inserted
                # AND the data shown responds to the well selected from the dropbox
                print(self.first_excel_dfs[0])
                self._load_table(self.first_excel_dfs[0])
                self.main_widget.table.show()
                self.resize(800, 600)
        except AttributeError:
            return QMessageBox.warning(self, "Error", "Archivo/s faltante/s.")

    def _cancel_button_logic(self):
        try:
            if len(self.first_excel_dfs) > 0 and len(self.second_excel_dfs) > 0:
                self._reset_button(1)
                self._reset_button(2)
        except AttributeError:
            try:
                if len(self.first_excel_dfs) > 0:
                    self._reset_button(1)
            except AttributeError:
                try:
                    if len(self.second_excel_dfs) > 0:
                        self._reset_button(2)
                except AttributeError:
                    return QMessageBox.warning(self, "Error", "No hay archivos para borrar.")