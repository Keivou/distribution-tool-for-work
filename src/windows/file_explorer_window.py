from PySide6.QtWidgets import QMainWindow


class FileExplorerWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("File Explorer")
        self.setCentralWidget(widget)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = self.file_menu.addAction("Exit", self.close)
        exit_action.setShortcut("Ctrl+Q")