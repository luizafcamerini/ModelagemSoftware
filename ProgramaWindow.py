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
        bd = Banco.get_instance().get_database()
        self.exercicios_col = bd["exercicios"]
        self.treino_col = bd["treinos"]
        self.programa_col = bd["programas"]

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
            nome_col = "Treino " + str(qtd_col)
            self.ui.tableWidget.setColumnCount(qtd_col+1)
            self.ui.tableWidget.setHorizontalHeaderItem(qtd_col, QTableWidgetItem(nome_col))
            selecionados = dlg.get_selected_items()
            
            linhas_selecionados = len(selecionados)
            if self.linhas < linhas_selecionados:
                self.linhas = linhas_selecionados
                self.ui.tableWidget.setRowCount(linhas_selecionados)

            for row, item in enumerate(selecionados):
                nome_item = QTableWidgetItem(item["nome"])
                nome_item.setData(Qt.UserRole, item['_id'])
                self.ui.tableWidget.setItem(row, qtd_col, nome_item)


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
        columnCount = self.ui.tableWidget.columnCount()

        for col in range(columnCount):
            col_info = dict()
            col_info["nome"] = self.ui.tableWidget.horizontalHeaderItem(col).text()
            col_info["exercicios"] = list()

            for row in range(rowCount):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    col_info["exercicios"].append(item.data(Qt.UserRole))
            treinos.append(col_info)

        insert_treinos = self.treino_col.insert_many(treinos)
        return list(insert_treinos.inserted_ids)



