from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QLabel, QPushButton, QGroupBox, QMessageBox
from PySide6.QtCore import Qt, Slot, Signal


class MainWidget(QWidget):

    # ------------------------------------------------------------------
    #                          CUSTOM SIGNALS
    # ------------------------------------------------------------------

    firstFileExplorerWindowRequested = Signal()
    secondFileExplorerWindowRequested = Signal()

    # ------------------------------------------------------------------
    #                               INIT
    # ------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        # Vertical Layout
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)
        
        # Elements
        (self.insert_button_1, self.insert_button_2) = self.insert_files_groupbox()

        # Signals
        self.insert_button_1.clicked.connect(self.request_first_file_explorer_window)
        self.insert_button_2.clicked.connect(self.request_second_file_explorer_window)

    # ------------------------------------------------------------------
    #                              SLOTS
    # ------------------------------------------------------------------

    @Slot()
    def request_first_file_explorer_window(self):
        self.firstFileExplorerWindowRequested.emit()

    @Slot()
    def request_second_file_explorer_window(self):
        self.secondFileExplorerWindowRequested.emit()

    # ------------------------------------------------------------------
    #                        INTERNAL FUNCTIONS
    # ------------------------------------------------------------------

    def insert_files_groupbox(self):
        # Groupbox
        groupBox = QGroupBox("Insertar archivos")

        # First insert
        first_hbox = QHBoxLayout()
        first_label = QLabel("Insertar primer archivo:")
        first_button = QPushButton("Insertar")
        first_hbox.addWidget(first_label)
        first_hbox.addWidget(first_button)
        first_hbox.setAlignment(Qt.AlignLeft)

        # Second insert
        second_hbox = QHBoxLayout()
        second_label = QLabel("Insertar segundo archivo:")
        second_button = QPushButton("Insertar")
        second_hbox.addWidget(second_label)
        second_hbox.addWidget(second_button)
        second_hbox.setAlignment(Qt.AlignLeft)

        # Vertical box
        vbox = QVBoxLayout()
        vbox.addLayout(first_hbox)
        vbox.addLayout(second_hbox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        self.vertical_layout.addWidget(groupBox)

        return first_button, second_button
    
    