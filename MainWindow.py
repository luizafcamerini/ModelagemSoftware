from ui_MainWindow import Ui_MainWindow
from PersonalWindow import PersonalWindow
from ClientWindow import ClienteWindow

from usuario import Usuario

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.personal_ui = PersonalWindow()
        self.cliente_ui = ClienteWindow()

        self.ui.setupUi(self)
        self.ui.alunoRadioButton.setChecked(True)
        self.ui.stackedWidget.insertWidget(1, self.personal_ui)
        self.ui.stackedWidget.insertWidget(2, self.cliente_ui)

        # Connects
        self.ui.entrarPushButton.clicked.connect(self.loginTriggered)
        self.personal_ui.logout.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.cliente_ui.logout.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

    Slot()
    def loginTriggered(self):
        if(self.validaUsuario(self.ui.cadastroLineEdit, self.ui.senhaLineEdit)):
            tipo = 1 if self.ui.alunoRadioButton.isChecked() else 2
            self.usuario = Usuario(self.ui.cadastroLineEdit, self.ui.senhaLineEdit, tipo)
            self.ui.stackedWidget.setCurrentIndex(tipo)
            


    def validaUsuario(self, nome, senha)-> bool:
        # pode ser da classe Usuario
        return True
