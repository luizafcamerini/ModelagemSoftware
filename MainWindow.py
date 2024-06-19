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
        self.init_banco()

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

    def init_banco(self):
        self.m_cliente = MongoClient("localhost", 27017, serverSelectionTimeoutMS=3000)
        self.bd = self.m_cliente["banco"]
        # self.colecao.insert_one({"campo1": 42, "campo2": 9001}) # pra inserir
        # documento = self.colecao.find_one({"campo1": 42}) # pra consultar
    
    Slot()
    def loginTriggered(self):
        if(self.validaUsuario(self.ui.cadastroLineEdit, self.ui.senhaLineEdit)):
            tipo = 1 if self.ui.alunoRadioButton.isChecked() else 2
            self.usuario = Usuario(self.ui.cadastroLineEdit, self.ui.senhaLineEdit, tipo)
            self.ui.stackedWidget.setCurrentIndex(tipo)
            


    def validaUsuario(self, nome, senha)-> bool:
        # pode ser da classe Usuario
        return True
