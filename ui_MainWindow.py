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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.loginWidget = QWidget(MainWindow)
        self.loginWidget.setObjectName(u"loginWidget")
        self.loginWidget.setGeometry(QRect(270, 51, 185, 151))
        self.formLayout = QFormLayout(self.loginWidget)
        self.formLayout.setObjectName(u"formLayout")
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer)

        self.label = QLabel(self.loginWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.entrarPushButton = QPushButton(self.loginWidget)
        self.entrarPushButton.setObjectName(u"entrarPushButton")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.entrarPushButton)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cadastroLabel.setText(QCoreApplication.translate("MainWindow", u"Cadastro: ", None))
        self.senhaLabel.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome do Aplicativo", None))
        self.entrarPushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
    # retranslateUi

