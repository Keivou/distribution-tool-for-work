from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class TableModel(QAbstractTableModel):

    # ------------------------------------------------------------------
    #                               INIT
    # ------------------------------------------------------------------

    def __init__(self, dataframe):
        super().__init__()
        self._df = dataframe

    # ------------------------------------------------------------------
    #                          MUST IMPLEMENT
    # ------------------------------------------------------------------

    def rowCount(self, parent=QModelIndex()):
        return len(self._df)

    def columnCount(self, parent=QModelIndex()):
        return len(self._df.columns)

    def data(self, index, role=Qt.DisplayRole):
        # Display data
        if role == Qt.DisplayRole:
            print("Display role:", index.row(), index.column())
            

    # ------------------------------------------------------------------
    #                       WELL BEHAVED MODEL?
    # ------------------------------------------------------------------

    # def headerData():
    #     pass

    # ------------------------------------------------------------------
    #                          EDITABLE MODEL
    # ------------------------------------------------------------------

    def setData(self, index, value, role=Qt.EditRole):
        if role in (Qt.DisplayRole, Qt.EditRole):
            print("Display/Edit role:", index.row(), index.column())
            # If value is blank
            if not value:
                return False
            self._df[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True

    def flags(self, index):
        return super().flags(index) | Qt.ItemIsEditable

    # The table IS NOT resizable
    # It will have X amount of Wells and 11 Columns, one for each of the inputs
