from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLabel
from PySide6.QtCore import Signal, Slot

class FileExplorerWidget(QWidget):

    # ------------------------------------------------------------------
    #                          CUSTOM SIGNALS
    # ------------------------------------------------------------------

    excelFileSelected = Signal()

    # ------------------------------------------------------------------
    #                               INIT
    # ------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        # Vertical Layout
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        # Adding field to layout
        self.file_name = self.insert_file_dialog()

        if self.file_name:
            self.excel_file_selected()
            

    # ------------------------------------------------------------------
    #                              SLOTS
    # ------------------------------------------------------------------


    # ------------------------------------------------------------------
    #                        INTERNAL FUNCTIONS
    # ------------------------------------------------------------------ 
    
    def excel_file_selected(self):
        self.excelFileSelected.emit()

    def insert_file_dialog(self):
        (file, filtr) = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx *.xls)")
        file_widget = QLabel(f"{file}")
        return file_widget.text()
            