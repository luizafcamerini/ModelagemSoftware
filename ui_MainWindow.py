# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.gridLayout_3 = QGridLayout(MainWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(MainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(200, 200, 200, 200)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.personalRadioButton = QRadioButton(self.page)
        self.personalRadioButton.setObjectName(u"personalRadioButton")

        self.verticalLayout_4.addWidget(self.personalRadioButton)

        self.alunoRadioButton = QRadioButton(self.page)
        self.alunoRadioButton.setObjectName(u"alunoRadioButton")

        self.verticalLayout_4.addWidget(self.alunoRadioButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.loginWidget = QWidget(self.page)
        self.loginWidget.setObjectName(u"loginWidget")
        self.formLayout = QFormLayout(self.loginWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.cadastroLabel = QLabel(self.loginWidget)
        self.cadastroLabel.setObjectName(u"cadastroLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cadastroLabel)

        self.cadastroLineEdit = QLineEdit(self.loginWidget)
        self.cadastroLineEdit.setObjectName(u"cadastroLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cadastroLineEdit)

        self.senhaLabel = QLabel(self.loginWidget)
        self.senhaLabel.setObjectName(u"senhaLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.senhaLabel)

        self.senhaLineEdit = QLineEdit(self.loginWidget)
        self.senhaLineEdit.setObjectName(u"senhaLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.senhaLineEdit)

        self.entrarPushButton = QPushButton(self.loginWidget)
        self.entrarPushButton.setObjectName(u"entrarPushButton")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.entrarPushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(0, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.loginWidget, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.personalRadioButton.setText(QCoreApplication.translate("MainWindow", u"Personal", None))
        self.alunoRadioButton.setText(QCoreApplication.translate("MainWindow", u"Aluno", None))
        self.cadastroLabel.setText(QCoreApplication.translate("MainWindow", u"Cadastro: ", None))
        self.senhaLabel.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.entrarPushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
    # retranslateUi

