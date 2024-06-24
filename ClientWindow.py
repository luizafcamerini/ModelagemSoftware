from bson import ObjectId
from ui_ClienteWindow import Ui_ClienteWindow
from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QLabel
from PySide6.QtCore import Signal, Slot, Qt
from banco import Banco

class ClienteWindow(QWidget):
    matricula = None
    nome = ""
    tabelas_treino = list()

    logout = Signal()
    sessao = Signal()
    solicitacao = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)

        bd = Banco.get_instance().get_database()
        self.programa_col = bd["programas"]
        self.treino_col = bd["treinos"]
        self.exercicio_col = bd["exercicios"]

        self.ui = Ui_ClienteWindow()
        self.ui.setupUi(self)
        # Connects
        self.ui.logout_button.clicked.connect(self.logoutClicked)
        self.ui.sessao_button.clicked.connect(self.sessaoClicked)
        # self.ui.solicitacao_button.clicked.connect(self.solicitacaoCriada)
    
    @Slot()
    def logoutClicked(self):
        self.matricula = None
        self.nome = ""
        self.remove_tabelas_de_treino()
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
    
    def setCurrentUser(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.lista_programa()        


    def lista_programa(self):
        programa = self.programa_col.find_one({"cliente": self.matricula})
        if programa:
            for treino_id in programa["treinos"]:
                self.cria_tabela_de_treino(treino_id)

    def cria_tabela_de_treino(self, treino_id):
        treino = self.treino_col.find_one({"_id": ObjectId(treino_id)})
        prog_layout = self.ui.programa_g_box.layout()
        tb_treino = QTableWidget()
        tb_treino.setColumnCount(2)
        tb_treino.setHorizontalHeaderLabels(["Nome", "Descrição"])
        tb_treino.setRowCount(len(treino["exercicios"]))

        for row, exec_id in enumerate(treino["exercicios"]):
            item = self.exercicio_col.find_one({"_id": exec_id})

            if item:
                print(item)
                nome_item = QTableWidgetItem(item["nome"])
                descricao_item = QTableWidgetItem(item["descricao"])
                
                nome_item.setFlags(nome_item.flags() & ~Qt.ItemIsEditable)
                descricao_item.setFlags(descricao_item.flags() & ~Qt.ItemIsEditable)

                tb_treino.setItem(row, 0, nome_item)
                tb_treino.setItem(row, 1, descricao_item)

        label = QLabel(treino["nome"])
        prog_layout.addWidget(label)
        prog_layout.addWidget(tb_treino)
        self.tabelas_treino.append(tb_treino)
        self.ui.programa_g_box.setLayout(prog_layout)

    def remove_tabelas_de_treino(self):
        prog_layout = self.ui.programa_g_box.layout()

        if prog_layout is not None:
            while self.tabelas_treino:
                tabela = self.tabelas_treino.pop()
                prog_layout.removeWidget(tabela)
                tabela.deleteLater() 