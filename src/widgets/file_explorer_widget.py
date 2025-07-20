from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog
from PySide6.QtCore import Qt, Slot, Signal

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

    #     # Signals and slots
    #     self.file_explorer_field.clicked.connect(self.save_excel_to_data)

    # @Slot()
    # def save_excel_to_data(file):
    #     with open(file, "w") as file:
    #         pass