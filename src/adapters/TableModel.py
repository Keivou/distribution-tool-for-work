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
            print("Display role:", self._df.iloc[index.row()], self._df.iloc[index.column() - 1])

            try:
                return str(self._df.iloc[index.row(), index.column()])
            except IndexError:
                return ""
            

    # ------------------------------------------------------------------
    #                       WELL BEHAVED MODEL?
    # ------------------------------------------------------------------

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # Only return data for the DisplayRole
        if role == Qt.DisplayRole:
            # If we need the horizontal headers (column names)
            if orientation == Qt.Horizontal:
                return str(self._df.columns[section])
            # If we need the vertical headers (row numbers)
            if orientation == Qt.Vertical:
                return str(self._df.index[section]) # Or return str(section + 1) for simple numbers

        # For any other role or orientation, return the default
        return super().headerData(section, orientation, role)

    # ------------------------------------------------------------------
    #                          EDITABLE MODEL
    # ------------------------------------------------------------------

    def setData(self, index, value, role=Qt.EditRole):
        if role in (Qt.DisplayRole, Qt.EditRole):
            print("Display/Edit role:", self._df.iloc[index.row()], self._df.iloc[index.column() - 1])
            # If value is blank
            if not value:
                return False
            self._df.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index)
            return True

    def flags(self, index):
        return super().flags(index) | Qt.ItemIsEditable

    # The table IS NOT resizable
    # It will have X amount of Wells and 11 Columns, one for each of the inputs

    # ------------------------------------------------------------------
    #                        INTERNAL FUNCTIONS
    # ------------------------------------------------------------------

    def _can_convert_to_float(self):
        pass

    def _can_convert_to_data(self):
        pass
