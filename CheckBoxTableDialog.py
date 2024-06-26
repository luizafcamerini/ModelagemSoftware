from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QApplication, QHeaderView, QCheckBox, QWidget
from PySide6.QtCore import Qt
import sys

class CheckboxTableDialog(QDialog):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Seleção de Exercícios")
        
        # Layout principal
        layout = QVBoxLayout(self)
        
        # Tabela com checkboxes
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nome", "Descrição", "Select"])
        
        self.tableWidget.setRowCount(len(items))
        for row, item in enumerate(items):
            id_item = QTableWidgetItem(str(item["_id"]))
            id_item.setData(Qt.UserRole, item['_id'])
            id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)

            nome_item = QTableWidgetItem(item["nome"])
            descricao_item = QTableWidgetItem(item["descricao"])
            
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
            self.tableWidget.setCellWidget(row, 3, checkbox_widget)
        
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
            checkbox_widget = self.tableWidget.cellWidget(row, 3)
            checkbox = checkbox_widget.layout().itemAt(0).widget()
            if checkbox.isChecked():
                item = {
                    "_id": self.tableWidget.item(row, 0).data(Qt.UserRole),
                    "nome": self.tableWidget.item(row, 1).text(),
                    "descricao": self.tableWidget.item(row, 2).text(),
                }
                selected_items.append(item)
        return selected_items
