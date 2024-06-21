# import datetime
from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui_ExercicioDialog import Ui_ExercicioDialog
from banco import Banco
# from ui_e
# class Programa():
#     __dataCriacao: datetime
#     __previsaoTermino: datetime
#     __id:int
#     __treinos:list
    
#     def __init__(self) -> None:
#         ...

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

        self.ui.tableWidget.setRowCount(linhas)
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(['id', 'nome', 'descricao', 'ilustracao'])
        if exercicios:
            for row, exercicio in enumerate(exercicios):
                print(exercicio)
                id_item = QTableWidgetItem(str(exercicio['id']))
                nome_item = QTableWidgetItem(exercicio['nome'])
                descricao_item = QTableWidgetItem(exercicio['descricao'])
                ilustracao_item = QTableWidgetItem(exercicio['ilustracao'])
                
                self.ui.tableWidget.setItem(row, 0, id_item)
                self.ui.tableWidget.setItem(row, 1, nome_item)
                self.ui.tableWidget.setItem(row, 2, descricao_item)
                self.ui.tableWidget.setItem(row, 3, ilustracao_item)
                self.exercicios.append({
                    "id": id_item.text(),
                    "nome": nome_item.text(),
                    "descricao": descricao_item.text(),
                    "ilustracao": ilustracao_item.text()
                })
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.salvar_button.clicked.connect(self.accept)
        self.ui.tableWidget.cellChanged.connect(self.adicionar_linha_se_necessario)

    def adicionar_linha_se_necessario(self, row, _):
        id_item = self.ui.tableWidget.item(row, 0)
        nome_item = self.ui.tableWidget.item(row, 1)
        desc_item = self.ui.tableWidget.item(row, 2)
        ilustracao_item = self.ui.tableWidget.item(row, 3)

        if (id_item and nome_item and desc_item and ilustracao_item ):
            row_count = self.ui.tableWidget.rowCount() + 1
            self.ui.tableWidget.setRowCount(row_count)
    
    def get_exercicios_alterados(self):
        alterados = []
        rowCount = self.ui.tableWidget.rowCount()
        columnCount = self.ui.tableWidget.columnCount()
        exerc_count = len(self.exercicios) - 1 
        for row in range(rowCount):
            linha_alterada = False
            for col in range(columnCount):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    if row <= exerc_count:
                        item_text = item.text()
                        coluna_nome = self.ui.tableWidget.horizontalHeaderItem(col).text()

                        if item_text != self.exercicios[row][coluna_nome]:
                            linha_alterada = True
                            break
                    else:
                        linha_alterada = True
            if linha_alterada:
                linha_info = {}
                for col in range(columnCount):
                    item = self.ui.tableWidget.item(row, col)
                    coluna_nome = self.ui.tableWidget.horizontalHeaderItem(col).text()
                    linha_info[coluna_nome] = item.text() if item else ""
                if not all(valor == "" for valor in linha_info.values()):
                    alterados.append(linha_info)

        for exercicio in alterados:
            print(exercicio)

        resultado = self.exercicios_col.insert_many(alterados)





