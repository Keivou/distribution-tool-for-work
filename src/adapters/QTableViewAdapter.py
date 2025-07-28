from PySide6.QtCore import QAbstractTableModel

class QtableViewAdapter(QAbstractTableModel):

    # ------------------------------------------------------------------
    #                               INIT
    # ------------------------------------------------------------------

    def __init__():
        super.__init__()

    # ------------------------------------------------------------------
    #                          MUST IMPLEMENT
    # ------------------------------------------------------------------

    def rowCount():
        pass

    def columnCount():
        pass

    def data():
        pass

    # ------------------------------------------------------------------
    #                       WELL BEHAVED MODEL?
    # ------------------------------------------------------------------

    def headerData():
        pass

    # ------------------------------------------------------------------
    #                          EDITABLE MODEL
    # ------------------------------------------------------------------

    def setData():
        pass

    def flags():
        pass

    # The table IS NOT resizable
    # It will have X amount of Wells and 11 Columns, one for each of the inputs
