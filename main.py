import subprocess
from MainWindow import MainWindow
from PySide6 import QtWidgets
import sys

def ui_convert():
    windowNames = ["ClienteWindow", "PersonalWindow", "MainWindow", "ExercicioDialog", "ProgramaWindow"]
    for name in windowNames:
        command1 = f"del ui_{name}.py"
        command2 = f"pyside6-uic {name}.ui -o ui_{name}.py"
        try:
            
            result = subprocess.run(command1, check=True, shell=True, stdout=subprocess.PIPE)
            result = subprocess.run(command2, check=True, shell=True, stdout=subprocess.PIPE)
            #print(f"Janela {name} atualizada")

        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o comando: {e}\n")

ui_convert()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.resize(1200, 800)

    window.show()
    
    sys.exit(app.exec())


