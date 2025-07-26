from PySide6.QtWidgets import QMainWindow


class FileExplorerWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("File Explorer")
        self.setCentralWidget(widget)