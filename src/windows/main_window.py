from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot

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

        # Exit QAction
        exit_action = self.file_menu.addAction("Salir", self.close)
        exit_action.setShortcut("Ctrl+Q")

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

    @Slot()
    def help_action(self):
        QMessageBox.about(self, "Ayuda", "Esta aplicación toma como input: xxx, y devuelve" \
        "las distribuciones de cada pozo.")


    


