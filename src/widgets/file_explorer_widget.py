from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog

class FileExplorerWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Vertical Layout
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        # File Explorer Field
        self.file_explorer_field = QFileDialog()

        # Adding field to layout
        self.vertical_layout.addWidget(self.file_explorer_field)