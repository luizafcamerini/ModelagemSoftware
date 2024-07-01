from bson import ObjectId
from ui_ClienteWindow import Ui_ClienteWindow
from PySide6.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem, 
                               QLabel, QToolButton,QHBoxLayout)
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtGui import QFont, QColor
from banco import Banco
from datetime import datetime

class ClienteWindow(QWidget):
    matricula = None
    nome = ""
    sessao_id = None
    tabelas_treino = list()
    labels = list()
    logout = Signal()
    sessao = Signal()
    solicitacao = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)

        bd = Banco.get_instance().get_database()
        self.programa_col = bd["programas"]
        self.treino_col = bd["treinos"]
        self.exercicio_col = bd["exercicios"]
        self.sessao_col = bd["sessao"]

        self.ui = Ui_ClienteWindow()
        self.ui.setupUi(self)

        self.ui.table_widget.setColumnCount(4)
        self.ui.table_widget.setHorizontalHeaderLabels(["Nome", "Séries", "Repetições", "Peso"])

        # Connects
        self.ui.logout_button.clicked.connect(self.logoutClicked)

        

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
        self.sessao_id = self.sessao_col.insert_one({
            "sessao_init": datetime.now(),
            "exercicios": []
        }).inserted_id


    def lista_programa(self):
        programa = self.programa_col.find_one({"cliente": self.matricula})
        if programa:
            for treino_id in programa["treinos"]:
                self.cria_tabela_de_treino(treino_id)

    def cria_tabela_de_treino(self, treino_id):
        treino = self.treino_col.find_one({"_id": ObjectId(treino_id)})
        prog_layout = self.ui.programa_g_box.layout()
        tb_treino = QTableWidget()
        tb_treino.setProperty("id", len(self.tabelas_treino))
        tb_treino.setColumnCount(6)
        tb_treino.setRowCount(len(treino))
        tb_treino.setHorizontalHeaderLabels(["", "Nome", "Séries", "Repetições", "Peso", "Descrição"])
        
        for row, exec in enumerate(treino["exercicios"]):
            item = self.exercicio_col.find_one({"_id": exec["id"]})
            if item:
                nome_item = QTableWidgetItem(item["nome"])
                nome_item.setData(Qt.UserRole, exec["id"])
                serie_item = QTableWidgetItem(exec["series"])
                rep_item = QTableWidgetItem(exec["repeticoes"])
                peso_item = QTableWidgetItem(exec["peso"])
                descricao_item = QTableWidgetItem(item["descricao"])
                
                nome_item.setFlags(nome_item.flags() & ~Qt.ItemIsEditable)
                serie_item.setFlags(nome_item.flags() & ~Qt.ItemIsEditable)
                rep_item.setFlags(nome_item.flags() & ~Qt.ItemIsEditable)
                peso_item.setFlags(nome_item.flags() & ~Qt.ItemIsEditable)
                descricao_item.setFlags(descricao_item.flags() & ~Qt.ItemIsEditable)

                button = QToolButton(tb_treino)
                button.setText("Concluir")
                button_widget = QWidget()
                button.setProperty("row", row)
                button.setProperty("tab", row)
                checkbox_layout = QHBoxLayout(button_widget)
                checkbox_layout.addWidget(button)
                checkbox_layout.setAlignment(Qt.AlignCenter)
                checkbox_layout.setContentsMargins(0, 0, 0, 0)
                button_widget.setLayout(checkbox_layout)

                tb_treino.setCellWidget(row, 0, button_widget)
                tb_treino.setItem(row, 1, nome_item)
                tb_treino.setItem(row, 2, serie_item)
                tb_treino.setItem(row, 3, rep_item)
                tb_treino.setItem(row, 4, peso_item)
                tb_treino.setItem(row, 5, descricao_item)
                
                button.clicked.connect(self.atualiza_sessao)


        label = QLabel(treino["nome"])
        self.labels.append(label)
        prog_layout.addWidget(label)
        prog_layout.addWidget(tb_treino)
        self.tabelas_treino.append(tb_treino)
        self.ui.programa_g_box.setLayout(prog_layout)
        
    def atualiza_sessao(self):
        button = self.sender()
        row = button.property("row")
        font = QFont()
        font.setBold(True)
        button.setEnabled(False)

        tab = button.parent().parent().parent()
        tb_sessao = self.ui.table_widget
        row_sessao = tb_sessao.rowCount() + 1
        tb_sessao.setRowCount(row_sessao)
        exec_info = dict()

        for i in range(5):
            item = tab.item(row, i + 1)
            item.setFont(font)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable & ~Qt.ItemIsSelectable & ~Qt.ItemIsEnabled)
            if i != 5:
                new_item = item.clone()
                new_item.setFlags(item.flags() | Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                tb_sessao.setItem(row_sessao - 1, i, new_item)
                col_name = ''
                if i==0:
                    col_name = "nome"
                    exec_info["id"] = new_item.data(Qt.UserRole)
                elif i==1:
                    col_name = "series"
                elif i == 2:
                    col_name = "repeticoes"
                elif i == 3:
                    col_name = "peso"
                if col_name != '':
                    exec_info[col_name] = new_item.text()
                print(i,"+", new_item.text())
        self.sessao_col.update_one(
            {'_id': self.sessao_id},
            {'cliente': self.matricula},
            { '$push': { "exercicios": exec_info }}
        )


        

    def remove_tabelas_de_treino(self):
        prog_layout = self.ui.programa_g_box.layout()

        if prog_layout is not None:
            while self.tabelas_treino:
                tabela = self.tabelas_treino.pop()
                label = self.labels.pop()
                prog_layout.removeWidget(tabela)
                prog_layout.removeWidget(label)
                tabela.deleteLater() 
                label.deleteLater()