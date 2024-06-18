from ui_PersonalWindow import Ui_PersonalWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot

class PersonalWindow(QWidget):
    logout = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PersonalWindow()
        self.ui.setupUi(self)

        # Connects
        self.ui.logoutQPushButton.clicked.connect(self.logoutClicked)

    @Slot()
    def logoutClicked(self):
        self.logout.emit()
