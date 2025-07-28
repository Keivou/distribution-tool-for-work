from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGroupBox, QTableView
from PySide6.QtCore import Qt, Slot, Signal


class MainWidget(QWidget):

    # ------------------------------------------------------------------
    #                          CUSTOM SIGNALS
    # ------------------------------------------------------------------

    fileExplorerWindowRequested = Signal(int)

    # ------------------------------------------------------------------
    #                               INIT
    # ------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        # Vertical Layout
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)
        
        # Elements
        (self.insert_button_1, self.insert_button_2) = self._insert_files_groupbox()
        self.qTable = self._insert_table()

        # Signals
        self.insert_button_1.clicked.connect(lambda: self.request_file_explorer_window(button=1))
        self.insert_button_2.clicked.connect(lambda: self.request_file_explorer_window(button=2))

    # ------------------------------------------------------------------
    #                              SLOTS
    # ------------------------------------------------------------------

    @Slot()
    def request_file_explorer_window(self, button: int):
        self.fileExplorerWindowRequested.emit(button)

    # ------------------------------------------------------------------
    #                        INTERNAL FUNCTIONS
    # ------------------------------------------------------------------

    def _insert_files_groupbox(self):
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
    
    def _insert_table(self):
        # Table
        table = QTableView()
        table.hide()

        # Vertical box
        vbox = QVBoxLayout()
        table.setLayout(vbox)
        self.vertical_layout.addWidget(table)

        return table
    