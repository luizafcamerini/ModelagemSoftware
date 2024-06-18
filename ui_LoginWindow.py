# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        self.gridLayoutWidget = QWidget(LoginWindow)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(200, 69, 341, 171))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.personalRadioButton = QRadioButton(self.gridLayoutWidget)
        self.personalRadioButton.setObjectName(u"personalRadioButton")

        self.verticalLayout_4.addWidget(self.personalRadioButton)

        self.alunoRadioButton = QRadioButton(self.gridLayoutWidget)
        self.alunoRadioButton.setObjectName(u"alunoRadioButton")

        self.verticalLayout_4.addWidget(self.alunoRadioButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.loginWidget = QWidget(self.gridLayoutWidget)
        self.loginWidget.setObjectName(u"loginWidget")
        self.formLayout = QFormLayout(self.loginWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.loginWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer)

        self.cadastroLabel = QLabel(self.loginWidget)
        self.cadastroLabel.setObjectName(u"cadastroLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cadastroLabel)

        self.cadastroLineEdit = QLineEdit(self.loginWidget)
        self.cadastroLineEdit.setObjectName(u"cadastroLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cadastroLineEdit)

        self.senhaLabel = QLabel(self.loginWidget)
        self.senhaLabel.setObjectName(u"senhaLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.senhaLabel)

        self.senhaLineEdit = QLineEdit(self.loginWidget)
        self.senhaLineEdit.setObjectName(u"senhaLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.senhaLineEdit)

        self.entrarPushButton = QPushButton(self.loginWidget)
        self.entrarPushButton.setObjectName(u"entrarPushButton")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.entrarPushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_4)


        self.gridLayout.addWidget(self.loginWidget, 0, 0, 1, 1)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.personalRadioButton.setText(QCoreApplication.translate("LoginWindow", u"Aluno", None))
        self.alunoRadioButton.setText(QCoreApplication.translate("LoginWindow", u"Personal", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Nome do Aplicativo", None))
        self.cadastroLabel.setText(QCoreApplication.translate("LoginWindow", u"Cadastro: ", None))
        self.senhaLabel.setText(QCoreApplication.translate("LoginWindow", u"Senha:", None))
        self.entrarPushButton.setText(QCoreApplication.translate("LoginWindow", u"Entrar", None))
    # retranslateUi

