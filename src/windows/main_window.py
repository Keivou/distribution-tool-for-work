from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from windows.file_explorer_window import FileExplorerWindow
from widgets.file_explorer_widget import FileExplorerWidget

class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("Distribution Tool")
        self.setCentralWidget(widget)
        widget.fileExplorerWindowRequested.connect(self.open_file_explorer_window)
        
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = self.file_menu.addAction("Exit", self.close)
        exit_action.setShortcut("Ctrl+Q")

    @Slot()
    def open_file_explorer_window(self, checked=True):
        self.file_explorer_widget = FileExplorerWidget()
        self.file_explorer_window = FileExplorerWindow(self.file_explorer_widget)
        self.file_explorer_window.resize(800, 600)
        self.file_explorer_window.show()

