from MainWindow import MainWindow
from PySide6 import QtWidgets, QtGui
import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())