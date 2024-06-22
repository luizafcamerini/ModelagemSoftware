from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QApplication, QHeaderView, QCheckBox, QWidget
from PySide6.QtCore import Qt
import sys

class CheckboxTableDialog(QDialog):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Checkbox Table Dialog")
        
        # Layout principal
        layout = QVBoxLayout(self)
        
        # Tabela com checkboxes
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nome", "Descrição", "Ilustração", "Select"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.tableWidget.setRowCount(len(items))
        for row, item in enumerate(items):
            id_item = QTableWidgetItem(str(item["_id"]))
            id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)

            nome_item = QTableWidgetItem(item["nome"])
            descricao_item = QTableWidgetItem(item["descricao"])
            ilustracao_item = QTableWidgetItem(item["ilustracao"])
            
            checkbox = QCheckBox()
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_widget.setLayout(checkbox_layout)

            self.tableWidget.setItem(row, 0, id_item)
            self.tableWidget.setItem(row, 1, nome_item)
            self.tableWidget.setItem(row, 2, descricao_item)
            self.tableWidget.setItem(row, 3, ilustracao_item)
            self.tableWidget.setCellWidget(row, 4, checkbox_widget)
        
        layout.addWidget(self.tableWidget)
        
        # Botões Cancelar e Salvar
        button_layout = QHBoxLayout()
        cancel_button = QPushButton("Cancelar")
        save_button = QPushButton("Salvar")
        
        cancel_button.clicked.connect(self.reject)
        save_button.clicked.connect(self.accept)
        
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        
        layout.addLayout(button_layout)
    
    def get_selected_items(self):
        selected_items = []
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            checkbox_widget = self.tableWidget.cellWidget(row, 4)
            checkbox = checkbox_widget.layout().itemAt(0).widget()
            if checkbox.isChecked():
                item = {
                    "_id": self.tableWidget.item(row, 0).text(),
                    "nome": self.tableWidget.item(row, 1).text(),
                    "descricao": self.tableWidget.item(row, 2).text(),
                    "ilustracao": self.tableWidget.item(row, 3).text()
                }
                selected_items.append(item)
        return selected_items

# # Código de teste
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
    
#     items = [
#         {"_id": "a", "nome": "b", "descricao": "c", "ilustracao": "d"},
#         {"_id": "e", "nome": "f", "descricao": "g", "ilustracao": "h"}
#     ]
    
#     dialog = CheckboxTableDialog(items)
#     if dialog.exec() == QDialog.Accepted:
#         selected_items = dialog.get_selected_items()
#         print("Selected items:", selected_items)
    
#     sys.exit(app.exec())
