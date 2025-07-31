from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QPushButton
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
        self.file_explorer_widget = FileExplorerWidget()
        self.file_explorer_window = FileExplorerWindow(self.file_explorer_widget)
        self.file_explorer_window.show()

        file_name = self.file_explorer_widget.file_name

        if self.file_explorer_widget.excelFileSelected:
            self.file_explorer_window.hide()
            if file_name != "" and button == 1:
                self.main_widget.insert_button_1.setEnabled(False)
                self.first_excel_df = self._load_excel(file_name)
                print(type(self.first_excel_df))

                data_model = TableModel(self.first_excel_df)
                self.main_widget.table.setModel(data_model)

                print(len(self.first_excel_df.columns))
            elif file_name != "" and button == 2:
                self.main_widget.insert_button_2.setEnabled(False)
                self.second_excel_df = self._load_excel(file_name)
                print(self.second_excel_df.head())

        if (not self.main_widget.insert_button_1.isEnabled() and 
            not self.main_widget.insert_button_2.isEnabled()):
            # Table only appears if the excels have already been inserted
            self.main_widget.table.show()
            self.resize(800, 600)

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
        
    def _load_excel(self, file_name):
        try:
            return pd.read_excel(file_name)
        except FileNotFoundError or ValueError:
            return
