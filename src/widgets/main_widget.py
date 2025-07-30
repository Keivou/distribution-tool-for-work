from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGroupBox, QTableView
from PySide6.QtCore import Qt, Slot, Signal
from adapters import TableModel


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
        self._insert_files_groupbox()
        self._insert_table()

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
        self.insert_button_1 = QPushButton("Insertar")
        first_hbox.addWidget(first_label)
        first_hbox.addWidget(self.insert_button_1)
        first_hbox.setAlignment(Qt.AlignLeft)

        # Second insert
        second_hbox = QHBoxLayout()
        second_label = QLabel("Insertar segundo archivo:")
        self.insert_button_2 = QPushButton("Insertar")
        second_hbox.addWidget(second_label)
        second_hbox.addWidget(self.insert_button_2)
        second_hbox.setAlignment(Qt.AlignLeft)

        # Vertical box
        vbox = QVBoxLayout()
        vbox.addLayout(first_hbox)
        vbox.addLayout(second_hbox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        self.vertical_layout.addWidget(groupBox)
    
    def _insert_table(self):
        # Table
        self.table = QTableView()
        self.vertical_layout.addWidget(self.table)

        # Table is hidden before the data is confirmed
        self.table.hide()
    