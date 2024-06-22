# import datetime
from PySide6.QtWidgets import QDialog, QTableWidgetItem
from PySide6 import QtCore
from ui_ProgramaWindow import Ui_ProgramaWindow
from banco import Banco
from PySide6.QtCore import Signal, Slot
from CheckBoxTableDialog import CheckboxTableDialog


class ProgramaWindow(QDialog, Banco):
    exercicios = []
    current_item: QTableWidgetItem
    def __init__(self, parent=None, exercicios = None):
        super().__init__(parent)
        self.exercicios = exercicios
        bd = Banco.get_instance().get_database()
        self.exercicios_col = bd["exercicios"]
        self.treino_col = bd["treinos"]
        self.ui = Ui_ProgramaWindow()
        self.ui.setupUi(self)

        linhas = 5
        self.ui.tableWidget.setRowCount(linhas)
        
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Treino 1', 'Treino 2', 'Treino'])

        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.salvar_button.clicked.connect(self.accept)
        self.ui.add_treino.clicked.connect(self.adiciona_treino)
        self.ui.del_treino.clicked.connect(self.deleta_treino)
        self.ui.add_linha.clicked.connect(self.adiciona_linha)
        self.ui.del_linha.clicked.connect(self.deleta_linha)
        
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
            nome_col = "Treino " + str(qtd_col)
            self.ui.tableWidget.setColumnCount(qtd_col+1)
            self.ui.tableWidget.setHorizontalHeaderItem(qtd_col, QTableWidgetItem(nome_col))
            selecionados = dlg.get_selected_items()
            for row, item in enumerate(selecionados):
                nome_item = QTableWidgetItem(item["nome"])
                nome_item.setData(QtCore.Qt.DisplayRole, item['_id'])
                self.ui.tableWidget.setItem(row, qtd_col, nome_item)


    def deleta_treino(self):
        self.ui.tableWidget.removeColumn(self.ui.tableWidget.currentColumn())
        print('deleta t')

    def adiciona_linha(self):
        qtd_rows = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(qtd_rows+1)

    def deleta_linha(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    def salva_programa(self):
        self.ui.cliente_edit.text()
        treinos = self.salva_treinos()
        # Todo: salvar id treino em programa
        pass

    def salva_treinos(self):
        treinos = list()

        rowCount = self.ui.tableWidget.rowCount()
        columnCount = self.ui.tableWidget.columnCount()

        for col in range(columnCount):
            col_info = dict()
            coluna_nome = self.ui.tableWidget.horizontalHeaderItem(col).text()

            for row in range(rowCount):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    col_info[coluna_nome] = item.text()
                    col_info["exercicio_id"] = str(item.data(QtCore.Qt.DisplayRole))
                treinos.append(col_info)

        self.treino_col.insert_many(treinos)
        return treinos






    


