from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("YPF Mami Tool")
        self.setCentralWidget(widget)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = self.file_menu.addAction("Exit", self.close)
        exit_action.setShortcut("Ctrl+Q")