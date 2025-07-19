import sys

from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QDateEdit, QFileDialog, QLabel, QPushButton
from PySide6.QtCore import Qt, Slot, Signal


class MainWidget(QWidget):
    # Custom Signals
    fileExplorerWindowRequested = Signal()


    def __init__(self):
        super().__init__()

        # Vertical Layout
        self.vertical_layout = QVBoxLayout()

        # Layers
        self.first_input_layer = QHBoxLayout()
        self.second_input_layer = QHBoxLayout()
        self.third_input_layer = QHBoxLayout()
        self.fourth_input_layer = QHBoxLayout()

        # Set the layout to the QWidget
        self.setLayout(self.vertical_layout)
        self.vertical_layout.addLayout(self.first_input_layer)
        self.vertical_layout.addLayout(self.second_input_layer)
        self.vertical_layout.addLayout(self.third_input_layer)
        self.vertical_layout.addLayout(self.fourth_input_layer)

        # # Name of the well
        # self.well_name_label = QLabel("Nombre del Pozo:")
        # self.well_name_field = QLineEdit()
        # self.well_name_field.setClearButtonEnabled(True)

        # # Number of wells
        # self.number_of_wells_label = QLabel("Número de Pozos:")
        # self.number_of_wells_field = QLineEdit()
        # self.number_of_wells_field.setClearButtonEnabled(True)

        # # Date
        # self.date_label = QLabel("Fecha:")
        # self.date_field = QDateEdit()
        # self.date_field.setCalendarPopup(True)

        # # "Punzadas" .xlsx file
        # self.insert_file_label = QLabel("Insertar archivo .xlsx:")
        # self.insert_file_field = QFileDialog()

        # Button for adding the first file
        self.insert_first_file_label = QLabel("Insertar archivo con Pozo, Fecha, Capa, Tope y Base:")
        self.insert_first_file_button = QPushButton("Abrir")

        # Adding the input fields
        self.first_input_layer.addWidget(self.insert_first_file_label)
        self.first_input_layer.addWidget(self.insert_first_file_button)

        # self.second_input_layer.addWidget(self.number_of_wells_label)
        # self.second_input_layer.addWidget(self.number_of_wells_field)

        # self.third_input_layer.addWidget(self.date_label)
        # self.third_input_layer.addWidget(self.date_field)

        # self.fourth_input_layer.addWidget(self.insert_file_label)
        # self.fourth_input_layer.addWidget(self.insert_file_field)

        # Signals and Slots
        self.insert_first_file_button.clicked.connect(self.request_file_explorer_window)

    @Slot()
    def request_file_explorer_window(self):
        self.fileExplorerWindowRequested.emit()