from ui_ClienteWindow import Ui_ClienteWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot

class ClienteWindow(QWidget):
    logout = Signal()
    sessao = Signal()
    solicitacao = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_ClienteWindow()
        self.ui.setupUi(self)

        # Connects
        self.ui.logout_button.clicked.connect(self.logoutClicked)
        self.ui.sessao_button.clicked.connect(self.sessaoClicked)
        # self.ui.solicitacao_button.clicked.connect(self.solicitacaoCriada)

    @Slot()
    def logoutClicked(self):
        self.logout.emit()
    
    @Slot()
    def sessaoClicked(self):
        self.sessao.emit()
    
    @Slot()
    def solicitacaoCriada(self):
        titulo = self.ui.titulo_text.text
        descricao = self.ui.descricao_text.text
        tipo = 1 if self.ui.exercicio_radiob else 2
        self.solicitacao.emit(titulo, descricao, tipo)
