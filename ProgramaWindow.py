# import datetime
from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui_ProgramaWindow import Ui_ProgramaWindow
from banco import Banco
from PySide6.QtCore import Signal, Slot, Qt
from CheckBoxTableDialog import CheckboxTableDialog


class ProgramaWindow(QDialog, Banco):
    exercicios = []
    linhas = 0
    current_item: QTableWidgetItem
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
        linhas = 1
        self.ui.tableWidget.setRowCount(linhas)

        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.salvar_button.clicked.connect(self.accept)
        self.ui.add_treino.clicked.connect(self.adiciona_treino)
        self.ui.del_treino.clicked.connect(self.deleta_treino)

    def lista_clientes(self, clientes):
        '''Popula combo box de clientes'''
        for cli in clientes:
            self.ui.cliente_c_box.addItem(cli["nome"] + cli["sobrenome"] + " - " + cli["matricula"], cli["matricula"])

    def adicionar_linha_se_necessario(self, row, _):
        '''Pular linha na tabela quando voce adiciona um exercicio'''
        id_item = self.ui.tableWidget.item(row, 0)
        nome_item = self.ui.tableWidget.item(row, 1)
        desc_item = self.ui.tableWidget.item(row, 2)
        ilustracao_item = self.ui.tableWidget.item(row, 3)

        if (id_item and nome_item and desc_item and ilustracao_item ):
            row_count = self.ui.tableWidget.rowCount() + 1
            self.ui.tableWidget.setRowCount(row_count)
            
    @Slot()
    def adiciona_treino(self):
        dlg = CheckboxTableDialog(self.exercicios)
        if (dlg.exec() == QDialog.Accepted):
            qtd_col = self.ui.tableWidget.columnCount()
            qtd_lin = self.ui.tableWidget.rowCount()
            print(qtd_lin)
            if qtd_col == 0:
                qtd_lin = 0
                self.ui.tableWidget.setColumnCount(qtd_col+4)
                self.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Exercícios"))
                self.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Séries"))
                self.ui.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Repetições"))
                self.ui.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Peso"))
            selecionados = dlg.get_selected_items()
            linhas_selecionados = len(selecionados)
            self.linhas = linhas_selecionados+qtd_lin+1
            self.ui.tableWidget.setRowCount(self.linhas)
            treino = QTableWidgetItem("Treino "+str(self.qtd_treinos))
            treino.textAlignment =  Qt.AlignmentFlag.AlignHCenter
            self.ui.tableWidget.setItem(qtd_lin, 0, treino)
            self.ui.tableWidget.setSpan(qtd_lin, 0, 1, 4)
            for row, item in enumerate(selecionados):
                nome_item = QTableWidgetItem(item["nome"])
                nome_item.setData(Qt.UserRole, item['_id'])
                nome_item.setFlags(nome_item.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(qtd_lin+1+row, 0, nome_item)

                series_item = QTableWidgetItem("3")
                series_item.setFlags(series_item.flags() | Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(qtd_lin+1+row, 1, series_item)

                repeticao_item = QTableWidgetItem("15")
                repeticao_item.setFlags(repeticao_item.flags() | Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(qtd_lin+1+row, 2, repeticao_item)

                peso_item = QTableWidgetItem("10")
                peso_item.setFlags(peso_item.flags() | Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(qtd_lin+1+row, 3, peso_item)

    def deleta_treino(self):
        self.ui.tableWidget.removeColumn(self.ui.tableWidget.currentColumn())
        print('deleta t')

    # def adiciona_linha(self):
    #     qtd_rows = self.ui.tableWidget.rowCount()
    #     self.ui.tableWidget.setRowCount(qtd_rows+1)

    # def deleta_linha(self):
    #     self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

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
        rowCount = self.ui.tableWidget.rowCount()
        i = 0
        info = dict()
        exercicios = list()
        while i < rowCount:
            item = self.ui.tableWidget.item(i, 0)
            if item.text().find("Treino") is not -1:
                if len(exercicios) is not 0:
                    info["exercicios"] = exercicios.copy()
                    treinos.append(info.copy())
                    exercicios.clear()
                    info.clear()
                info["name"] = item.text()
            elif item is not None:
                exercicio = dict()
                exercicio["id"] = item.data(Qt.UserRole)
                serie_item = self.ui.tableWidget.item(i, 1)
                repeticao_item = self.ui.tableWidget.item(i, 2)
                peso_item = self.ui.tableWidget.item(i, 3)
                exercicio["series"] = serie_item.text()
                exercicio["repeticoes"] = repeticao_item.text()
                exercicio["peso"] = peso_item.text()
                print(exercicio)
                exercicios.append(exercicio)
                print(exercicios)
            i += 1
        if len(exercicios) is not 0:
            info["exercicios"] = exercicios.copy()
            treinos.append(info.copy())
            exercicios.clear()
            info.clear()
            print(treinos)

        insert_treinos = self.treino_col.insert_many(treinos)
        return list(insert_treinos.inserted_ids)
