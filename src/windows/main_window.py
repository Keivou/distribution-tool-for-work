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
        self.setCentralWidget(widget)

        # Signals
        widget.fileExplorerWindowRequested.connect(self.open_file_explorer_window)
        
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Archivo")
        self.help_menu = self.menu.addMenu("Ayuda")

        ## File Menu

        # Exit QAction
        exit_action = self.file_menu.addAction("Salir", self.close)
        exit_action.setShortcut("Ctrl+Q")

        # Load QAction
        load_action = self.file_menu.addAction("Abrir", self.load_action)

        ## Help Menu

        # Help QAction
        help_action = self.help_menu.addAction("Ayuda", self.help_action)
        help_action.setShortcut("Ctrl+H")


    # ------------------------------------------------------------------
    #                              SLOTS
    # ------------------------------------------------------------------

    @Slot()
    def open_file_explorer_window(self):
        self.file_explorer_widget = FileExplorerWidget()
        self.file_explorer_window = FileExplorerWindow(self.file_explorer_widget)
        self.file_explorer_window.show()
        self.file_name = self.file_explorer_widget.file_name

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

    


