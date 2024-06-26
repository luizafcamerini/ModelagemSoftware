# import datetime
from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QLabel, QScrollArea
from bson import ObjectId
from ui_ProgramaWindow import Ui_ProgramaWindow
from banco import Banco
from PySide6.QtCore import Signal, Slot, Qt
from CheckBoxTableDialog import CheckboxTableDialog


class ProgramaWindow(QDialog, Banco):
    exercicios = []
    linhas = 0
    current_item: QTableWidgetItem
    tabelas_treino = list()

    def __init__(self, parent=None, exercicios = None, clientes = None):
        super().__init__(parent)

        self.exercicios = exercicios
        self.qtd_treinos = 0
        bd = Banco.get_instance().get_database()
        self.exercicios_col = bd["exercicios"]
        self.treino_col = bd["treinos"]
        self.programa_col = bd["programas"]
        self.linhas = 0

        self.ui = Ui_ProgramaWindow()
        self.ui.setupUi(self)
        self.lista_clientes(clientes)

        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.salvar_button.clicked.connect(self.accept)
        self.ui.add_treino.clicked.connect(self.adiciona_treino)
        
    def lista_clientes(self, clientes):
        '''Popula combo box de clientes'''
        for cli in clientes:
            self.ui.cliente_c_box.addItem(cli["nome"] + cli["sobrenome"] + " - " + cli["matricula"], cli["matricula"])
            
    @Slot()
    def adiciona_treino(self):
        dlg = CheckboxTableDialog(self.exercicios)
        if (dlg.exec() == QDialog.Accepted):
            self.cria_tabela_treino(dlg.get_selected_items())

    def cria_tabela_treino(self, exercicios):
        prog_layout = self.ui.programa_layout
        tb_treino = QTableWidget()
        tb_treino.setColumnCount(4)
        tb_treino.setHorizontalHeaderLabels(["Exercício", "Séries", "Repetições", "Peso"])

        linhas_selecionados = len(exercicios)
        tb_treino.setRowCount(linhas_selecionados)
        self.qtd_treinos += 1
        treino_name = "Treino "+str(self.qtd_treinos)

        for row, item in enumerate(exercicios):
            nome_item = QTableWidgetItem(item["nome"])
            nome_item.setData(Qt.UserRole, item['_id'])
            nome_item.setFlags(nome_item.flags() & ~Qt.ItemIsEditable)
            tb_treino.setItem(row, 0, nome_item)

            series_item = QTableWidgetItem("3")
            series_item.setFlags(series_item.flags() | Qt.ItemIsEditable)
            tb_treino.setItem(row, 1, series_item)

            repeticao_item = QTableWidgetItem("15")
            repeticao_item.setFlags(repeticao_item.flags() | Qt.ItemIsEditable)
            tb_treino.setItem(row, 2, repeticao_item)

            peso_item = QTableWidgetItem("10")
            peso_item.setFlags(peso_item.flags() | Qt.ItemIsEditable)
            tb_treino.setItem(row, 3, peso_item)

        label = QLabel(treino_name)
        prog_layout.addWidget(label)
        prog_layout.addWidget(tb_treino)
        self.tabelas_treino.append({"label": treino_name, "tab": tb_treino})

    def salva_programa(self):
        cliente = self.ui.cliente_c_box.currentData(Qt.UserRole)
        if(cliente):
            programa = {
                "treinos": self.salva_treinos(),
                "cliente": cliente
            }
            self.programa_col.insert_one(programa)
            

    def salva_treinos(self):
        treinos = list()

        for lista in self.tabelas_treino:
            info_treino = dict()
            exercicios = list()
            info_treino["nome"] = lista["label"]
            treino = lista["tab"]
            rowCount = treino.rowCount()
            for i in range(rowCount):
                item = treino.item(i, 0)
                if item is not None and item.text():
                    exercicio = dict()
                    exercicio["id"] = item.data(Qt.UserRole)
                    serie_item = treino.item(i, 1)
                    repeticao_item = treino.item(i, 2)
                    peso_item = treino.item(i, 3)
                    exercicio["series"] = serie_item.text()
                    exercicio["repeticoes"] = repeticao_item.text()
                    exercicio["peso"] = peso_item.text()
                    exercicios.append(exercicio)
            info_treino["exercicios"] = exercicios.copy()
            treinos.append(info_treino)
        insert_treinos = self.treino_col.insert_many(treinos)
        return list(insert_treinos.inserted_ids)
