from banco import Banco
from ui_MainWindow import Ui_MainWindow

from PersonalWindow import PersonalWindow
from ClientWindow import ClienteWindow
from ExercicioDialog import ExercicioDialog
from ProgramaWindow import ProgramaWindow


from PySide6.QtWidgets import QWidget, QDialog
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
        self.connects()
    
    def connects(self):
        self.ui.entrarPushButton.clicked.connect(self.loginTriggered)
        self.personal_ui.logout.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.cliente_ui.logout.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.personal_ui.cad_exercicio.connect(self.exercicio_dlg)
        self.personal_ui.cria_programa.connect(self.programa_dlg)

    Slot()
    def loginTriggered(self):
        tipo = 2 if self.ui.alunoRadioButton.isChecked() else 1
        if(self.validaUsuario(self.ui.cadastroLineEdit.text(), self.ui.senhaLineEdit.text(), tipo)):
            self.ui.stackedWidget.setCurrentIndex(tipo)

    @Slot(list)
    def exercicio_dlg(self, exercicios):
        dlg = ExercicioDialog(self, exercicios)
        if (dlg.exec() == QDialog.Accepted):
            dlg.salva_alteracoes()

    @Slot(list)
    def programa_dlg(self, exercicios):
        dlg = ProgramaWindow(self, exercicios)
        if (dlg.exec() == QDialog.Accepted):
            dlg.salva_programa()

    def validaUsuario(self, nome, senha, cargo)-> bool:
        # pode ser da classe Usuario
        col = None
        if cargo == 2:
            col = self.banco["clientes"]
        else:
            col = self.banco["personais"]
        user = col.find_one({"matricula":str(nome)})
        if user and user["senha"] == senha:
            if(cargo == 1):
                self.personal_ui.setCurrentUser(user["matricula"], user["senha"])
            else:
                pass

            return True
        return False
    