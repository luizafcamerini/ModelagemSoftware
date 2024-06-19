from banco import Banco
from ui_MainWindow import Ui_MainWindow
from PersonalWindow import PersonalWindow
from ClientWindow import ClienteWindow

from usuario import Usuario

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from pymongo import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.banco = Banco.get_instance().get_database()
        self.usuario = None

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
        tipo = 1 if self.ui.alunoRadioButton.isChecked() else 2
        if(self.validaUsuario(self.ui.cadastroLineEdit.text(), self.ui.senhaLineEdit.text(), tipo)):
            self.usuario = Usuario(self.ui.cadastroLineEdit.text(), self.ui.senhaLineEdit.text(), tipo)
            self.ui.stackedWidget.setCurrentIndex(tipo)
            


    def validaUsuario(self, nome, senha, cargo)-> bool:
        # pode ser da classe Usuario
        col = None
        if cargo == 1:
            col = self.banco["clientes"]
        else:
            col = self.banco["personais"]
        user = col.find_one({"matricula":str(nome)})
        if user and user["senha"] == senha:
            return True
        return False
