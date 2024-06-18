# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClienteWindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

class Ui_ClienteWindow(object):
    def setupUi(self, ClienteWindow):
        if not ClienteWindow.objectName():
            ClienteWindow.setObjectName(u"ClienteWindow")
        ClienteWindow.resize(800, 600)
        self.pushButton = QPushButton(ClienteWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 10, 80, 24))
        self.groupBox = QGroupBox(ClienteWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 221, 511))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.listWidget_2 = QListWidget(self.groupBox)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.gridLayout_3.addWidget(self.listWidget_2, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(ClienteWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(230, 10, 280, 511))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listWidget_3 = QListWidget(self.groupBox_2)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.gridLayout_4.addWidget(self.listWidget_3, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(ClienteWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(522, 90, 271, 183))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 3, 0, 1, 2)

        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 3, 2, 1, 1)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 2)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.tab_2)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.logoutQPushButton = QPushButton(ClienteWindow)
        self.logoutQPushButton.setObjectName(u"logoutQPushButton")
        self.logoutQPushButton.setGeometry(QRect(710, 10, 80, 24))

        self.retranslateUi(ClienteWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ClienteWindow)
    # setupUi

    def retranslateUi(self, ClienteWindow):
        ClienteWindow.setWindowTitle(QCoreApplication.translate("ClienteWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("ClienteWindow", u"Iniciar Sess\u00e3o", None))
        self.groupBox.setTitle(QCoreApplication.translate("ClienteWindow", u"Meu Programa", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ClienteWindow", u"Exerc\u00edcios da Sess\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("ClienteWindow", u"Descri\u00e7\u00e3o:", None))
        self.radioButton.setText(QCoreApplication.translate("ClienteWindow", u"Alterar exerc\u00edcio", None))
        self.radioButton_2.setText(QCoreApplication.translate("ClienteWindow", u"Alterar treino", None))
        self.label.setText(QCoreApplication.translate("ClienteWindow", u"T\u00edtulo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ClienteWindow", u"Criar Solicita\u00e7\u00e3o", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ClienteWindow", u"Minhas Solicita\u00e7\u00f5es", None))
        self.logoutQPushButton.setText(QCoreApplication.translate("ClienteWindow", u"Logout", None))
    # retranslateUi

