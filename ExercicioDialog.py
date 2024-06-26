# import datetime
from PySide6.QtWidgets import QDialog, QTableWidgetItem
from PySide6 import QtCore
from ui_ExercicioDialog import Ui_ExercicioDialog
from banco import Banco

class ExercicioDialog(QDialog, Banco):
    exercicios = []
    def __init__(self, parent=None, exercicios = None):
        super().__init__(parent)
        
        bd = Banco.get_instance().get_database()
        self.exercicios_col = bd["exercicios"]

        self.ui = Ui_ExercicioDialog()
        self.ui.setupUi(self)
        linhas = 1

        if exercicios:
            linhas += len(exercicios)
        else:
            self.exercicios = exercicios if exercicios else []

        new_item = QTableWidgetItem("")
        new_item.setFlags(new_item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.ui.tableWidget.setItem(linhas, 0, new_item)

        self.ui.tableWidget.setRowCount(linhas)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['_id', 'nome', 'descricao'])
        if exercicios:
            self.lista_exercicios(exercicios)
            
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.salvar_button.clicked.connect(self.accept)
        self.ui.tableWidget.cellChanged.connect(self.adicionar_linha_se_necessario)
    
    def lista_exercicios(self, exercicios):
        for row, exercicio in enumerate(exercicios):
            id_item = QTableWidgetItem(str(exercicio['_id']))
            id_item.setFlags(id_item.flags() & ~QtCore.Qt.ItemIsEditable)
            nome_item = QTableWidgetItem(exercicio['nome'])
            descricao_item = QTableWidgetItem(exercicio['descricao'])
            
            self.ui.tableWidget.setItem(row, 0, id_item)
            self.ui.tableWidget.setItem(row, 1, nome_item)
            self.ui.tableWidget.setItem(row, 2, descricao_item)
            self.exercicios.append({
                "id": id_item.text(),
                "nome": nome_item.text(),
                "descricao": descricao_item.text(),
            })

    def adicionar_linha_se_necessario(self, row, _):
        '''Pular linha na tabela quando voce adiciona um exercicio'''
        id_item = self.ui.tableWidget.item(row, 0)
        nome_item = self.ui.tableWidget.item(row, 1)
        desc_item = self.ui.tableWidget.item(row, 2)

        if (id_item and nome_item and desc_item ):
            row_count = self.ui.tableWidget.rowCount() + 1
            self.ui.tableWidget.setRowCount(row_count)
            new_item = QTableWidgetItem("")
            new_item.setFlags(new_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row_count, 0, new_item)

    
    def salva_alteracoes(self):
        alterados = list()
        adicionados = list()

        rowCount = self.ui.tableWidget.rowCount()
        columnCount = self.ui.tableWidget.columnCount()
        exerc_count = len(self.exercicios) - 1

        for row in range(rowCount):
            linha_alterada = False
            linha_adicionada = False
            for col in range(columnCount):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    if row <= exerc_count:
                        item_text = item.text()
                        coluna_nome = self.ui.tableWidget.horizontalHeaderItem(col).text()

                        if coluna_nome != "_id" and item_text != self.exercicios[row][coluna_nome]:
                            linha_alterada = True
                            break
                    else:
                        linha_adicionada = True

            if linha_alterada or linha_adicionada:
                linha_info = {}
                for col in range(columnCount):
                    item = self.ui.tableWidget.item(row, col)
                    coluna_nome = self.ui.tableWidget.horizontalHeaderItem(col).text()
                    if coluna_nome != "_id":
                        linha_info[coluna_nome] = item.text() if item else ""
                if linha_alterada:
                    if not all(valor == "" for valor in linha_info.values()):
                        alterados.append(linha_info)
                if linha_adicionada:
                    if not all(valor == "" for valor in linha_info.values()):
                        adicionados.append(linha_info)
        for i in alterados:
            self.exercicios_col.update_one(
                {'_id': i['_id']},
                {'$set': i}
            )
        self.exercicios_col.insert_many(adicionados)

