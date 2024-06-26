# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgramaWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_ProgramaWindow(object):
    def setupUi(self, ProgramaWindow):
        if not ProgramaWindow.objectName():
            ProgramaWindow.setObjectName(u"ProgramaWindow")
        ProgramaWindow.resize(636, 497)
        self.gridLayout_3 = QGridLayout(ProgramaWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cliente_c_box = QComboBox(ProgramaWindow)
        self.cliente_c_box.setObjectName(u"cliente_c_box")

        self.gridLayout_2.addWidget(self.cliente_c_box, 0, 1, 1, 2)

        self.cliente_label = QLabel(ProgramaWindow)
        self.cliente_label.setObjectName(u"cliente_label")

        self.gridLayout_2.addWidget(self.cliente_label, 0, 0, 1, 1)

        self.add_treino = QToolButton(ProgramaWindow)
        self.add_treino.setObjectName(u"add_treino")

        self.gridLayout_2.addWidget(self.add_treino, 0, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 6, 0, 1, 3)

        self.cancel_button = QPushButton(ProgramaWindow)
        self.cancel_button.setObjectName(u"cancel_button")

        self.gridLayout_2.addWidget(self.cancel_button, 6, 3, 1, 1)

        self.scrollArea = QScrollArea(ProgramaWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 528, 415))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.programa_layout = QVBoxLayout()
        self.programa_layout.setObjectName(u"programa_layout")

        self.gridLayout_4.addLayout(self.programa_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 3, 4)

        self.salvar_button = QPushButton(ProgramaWindow)
        self.salvar_button.setObjectName(u"salvar_button")

        self.gridLayout_2.addWidget(self.salvar_button, 6, 4, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(ProgramaWindow)

        QMetaObject.connectSlotsByName(ProgramaWindow)
    # setupUi

    def retranslateUi(self, ProgramaWindow):
        ProgramaWindow.setWindowTitle(QCoreApplication.translate("ProgramaWindow", u"MainWindow", None))
        self.cliente_label.setText(QCoreApplication.translate("ProgramaWindow", u"Cliente", None))
        self.add_treino.setText(QCoreApplication.translate("ProgramaWindow", u"Add Treino", None))
        self.cancel_button.setText(QCoreApplication.translate("ProgramaWindow", u"cancel", None))
        self.salvar_button.setText(QCoreApplication.translate("ProgramaWindow", u"Salvar", None))
    # retranslateUi

