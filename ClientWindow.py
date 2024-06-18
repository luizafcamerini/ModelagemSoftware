from ui_ClienteWindow import Ui_ClienteWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot

class ClienteWindow(QWidget):
    logout = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_ClienteWindow()
        self.ui.setupUi(self)

        # Connects
        self.ui.logoutQPushButton.clicked.connect(self.logoutClicked)

    @Slot()
    def logoutClicked(self):
        self.logout.emit()
