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
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_ClienteWindow(object):
    def setupUi(self, ClienteWindow):
        if not ClienteWindow.objectName():
            ClienteWindow.setObjectName(u"ClienteWindow")
        ClienteWindow.resize(800, 600)
        self.gridLayout_5 = QGridLayout(ClienteWindow)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget = QStackedWidget(ClienteWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 70, 271, 183))
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

        self.exercicio_radiob = QRadioButton(self.frame)
        self.exercicio_radiob.setObjectName(u"exercicio_radiob")

        self.gridLayout.addWidget(self.exercicio_radiob, 3, 0, 1, 2)

        self.treino_radiob = QRadioButton(self.frame)
        self.treino_radiob.setObjectName(u"treino_radiob")

        self.gridLayout.addWidget(self.treino_radiob, 3, 2, 1, 1)

        self.descricao_text = QTextEdit(self.frame)
        self.descricao_text.setObjectName(u"descricao_text")

        self.gridLayout.addWidget(self.descricao_text, 1, 1, 1, 2)

        self.solicitacao_button = QDialogButtonBox(self.frame)
        self.solicitacao_button.setObjectName(u"solicitacao_button")
        self.solicitacao_button.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.solicitacao_button, 4, 2, 1, 1)

        self.titulo_text = QLineEdit(self.frame)
        self.titulo_text.setObjectName(u"titulo_text")

        self.gridLayout.addWidget(self.titulo_text, 0, 1, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.solicitacoes_list = QListWidget(self.tab_2)
        self.solicitacoes_list.setObjectName(u"solicitacoes_list")

        self.horizontalLayout.addWidget(self.solicitacoes_list)

        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_2 = QHBoxLayout(self.page_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.page_4)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.page_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.exercicios_sessao_list = QListWidget(self.groupBox_2)
        self.exercicios_sessao_list.setObjectName(u"exercicios_sessao_list")

        self.gridLayout_4.addWidget(self.exercicios_sessao_list, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.sessao_button = QPushButton(self.page_4)
        self.sessao_button.setObjectName(u"sessao_button")

        self.gridLayout_7.addWidget(self.sessao_button, 0, 0, 1, 1)

        self.logout_button = QPushButton(self.page_4)
        self.logout_button.setObjectName(u"logout_button")

        self.gridLayout_7.addWidget(self.logout_button, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_7)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(ClienteWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ClienteWindow)
    # setupUi

    def retranslateUi(self, ClienteWindow):
        ClienteWindow.setWindowTitle(QCoreApplication.translate("ClienteWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("ClienteWindow", u"Descri\u00e7\u00e3o:", None))
        self.exercicio_radiob.setText(QCoreApplication.translate("ClienteWindow", u"Alterar exerc\u00edcio", None))
        self.treino_radiob.setText(QCoreApplication.translate("ClienteWindow", u"Alterar treino", None))
        self.label.setText(QCoreApplication.translate("ClienteWindow", u"T\u00edtulo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ClienteWindow", u"Criar Solicita\u00e7\u00e3o", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ClienteWindow", u"Minhas Solicita\u00e7\u00f5es", None))
        self.groupBox.setTitle(QCoreApplication.translate("ClienteWindow", u"Meu Programa", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ClienteWindow", u"Exerc\u00edcios da Sess\u00e3o", None))
        self.sessao_button.setText(QCoreApplication.translate("ClienteWindow", u"Iniciar Sess\u00e3o", None))
        self.logout_button.setText(QCoreApplication.translate("ClienteWindow", u"Logout", None))
    # retranslateUi

