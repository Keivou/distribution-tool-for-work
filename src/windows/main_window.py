from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide6.QtCore import Slot, QFile, Qt, QTextStream

from windows.file_explorer_window import FileExplorerWindow
from widgets.file_explorer_widget import FileExplorerWidget

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
        self.main_widget.firstFileExplorerWindowRequested.connect(self.open_first_file_explorer_window)
        self.main_widget.secondFileExplorerWindowRequested.connect(self.open_second_file_explorer_window)
        
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Archivo")
        self.help_menu = self.menu.addMenu("Ayuda")

        ## File Menu

        # Exit QAction
        exit_action = self.file_menu.addAction("Salir", self.close)
        exit_action.setShortcut("Ctrl+Q")

        # Load QAction
        self.file_menu.addAction("Cargar", self.load_action)

        ## Help Menu

        # Help QAction
        help_action = self.help_menu.addAction("Ayuda", self.help_action)
        help_action.setShortcut("Ctrl+H")


    # ------------------------------------------------------------------
    #                              SLOTS
    # ------------------------------------------------------------------

    @Slot()
    def open_first_file_explorer_window(self):
        self.first_file_explorer_widget = FileExplorerWidget()
        self.first_file_explorer_window = FileExplorerWindow(self.first_file_explorer_widget)
        self.first_file_explorer_window.show()

        self.file_name = self.first_file_explorer_widget.file_name

        if self.first_file_explorer_widget.excelFileSelected:
            self.first_file_explorer_window.hide()
            self.main_widget.insert_button_1.setEnabled(False)

    @Slot()
    def open_second_file_explorer_window(self):
        self.second_file_explorer_widget = FileExplorerWidget()
        self.second_file_explorer_window = FileExplorerWindow(self.second_file_explorer_widget)
        self.second_file_explorer_window.show()

        self.file_name = self.second_file_explorer_widget.file_name

        if self.second_file_explorer_widget.excelFileSelected:
            self.second_file_explorer_window.hide()
            self.main_widget.insert_button_2.setEnabled(False)

    @Slot()
    def help_action(self):
        QMessageBox.about(self, "Ayuda", "Esta aplicación toma como input: xxx, y devuelve" \
        "las distribuciones de cada pozo.")

    # NOT QUITE THE RIGHT APPLICATION, BUT GOOD FOR TESTING FOR NOW
    @Slot()
    def load_action(self):
        file = QFile(self.file_name)

        if not file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            reason = file.errorString()
            QMessageBox.warning(self, "Application", f"Cannot read file {self.file_name}:\n{reason}.")
            return

        info = QTextStream(file)
        with QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor):
            print(info.readAll()) # <- DO SOMETHING ELSE INSTEAD OF PRINTING

    


