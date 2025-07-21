from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLabel
from PySide6.QtCore import Qt, Slot, QStringListModel

class FileExplorerWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Vertical Layout
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        # Adding field to layout
        self.vertical_layout.addWidget(self.get_file_name())

        # Signals and slots
        # self.file.clicked.connect(self.save_excel_to_data)

    def get_file_name(self):
        (file, filtr) = QFileDialog.getOpenFileName()
        file_widget = QLabel(f"{file}")
        return file_widget