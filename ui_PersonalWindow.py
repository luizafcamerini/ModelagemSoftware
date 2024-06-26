# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PersonalWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_PersonalWindow(object):
    def setupUi(self, PersonalWindow):
        if not PersonalWindow.objectName():
            PersonalWindow.setObjectName(u"PersonalWindow")
        PersonalWindow.resize(800, 600)
        self.gridLayout_3 = QGridLayout(PersonalWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(200)
        self.gridLayout_3.setContentsMargins(200, 200, 200, 200)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.cad_exercicio_button = QPushButton(PersonalWindow)
        self.cad_exercicio_button.setObjectName(u"cad_exercicio_button")

        self.gridLayout_8.addWidget(self.cad_exercicio_button, 3, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.programa_button = QPushButton(PersonalWindow)
        self.programa_button.setObjectName(u"programa_button")

        self.gridLayout_8.addWidget(self.programa_button, 2, 0, 1, 3)


        self.gridLayout_3.addLayout(self.gridLayout_8, 0, 0, 1, 2)

        self.logout_button = QPushButton(PersonalWindow)
        self.logout_button.setObjectName(u"logout_button")

        self.gridLayout_3.addWidget(self.logout_button, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.retranslateUi(PersonalWindow)

        QMetaObject.connectSlotsByName(PersonalWindow)
    # setupUi

    def retranslateUi(self, PersonalWindow):
        PersonalWindow.setWindowTitle(QCoreApplication.translate("PersonalWindow", u"MainWindow", None))
        self.cad_exercicio_button.setText(QCoreApplication.translate("PersonalWindow", u"Cadastrar Excerc\u00edcio", None))
        self.programa_button.setText(QCoreApplication.translate("PersonalWindow", u"Criar Programa", None))
        self.logout_button.setText(QCoreApplication.translate("PersonalWindow", u"logout", None))
    # retranslateUi

