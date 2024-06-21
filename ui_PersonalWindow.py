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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QWidget)

class Ui_PersonalWindow(object):
    def setupUi(self, PersonalWindow):
        if not PersonalWindow.objectName():
            PersonalWindow.setObjectName(u"PersonalWindow")
        PersonalWindow.resize(800, 600)
        self.gridLayout_3 = QGridLayout(PersonalWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.groupBox_2 = QGroupBox(PersonalWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_7 = QGridLayout(self.tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pendentes_list = QListView(self.tab)
        self.pendentes_list.setObjectName(u"pendentes_list")

        self.gridLayout_7.addWidget(self.pendentes_list, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.respondidas_list = QListView(self.tab_2)
        self.respondidas_list.setObjectName(u"respondidas_list")

        self.gridLayout_2.addWidget(self.respondidas_list, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.cadastrar_button = QPushButton(PersonalWindow)
        self.cadastrar_button.setObjectName(u"cadastrar_button")

        self.gridLayout_8.addWidget(self.cadastrar_button, 2, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.logout_button = QPushButton(PersonalWindow)
        self.logout_button.setObjectName(u"logout_button")

        self.gridLayout_8.addWidget(self.logout_button, 1, 1, 1, 1)

        self.configurar_treino_button = QPushButton(PersonalWindow)
        self.configurar_treino_button.setObjectName(u"configurar_treino_button")

        self.gridLayout_8.addWidget(self.configurar_treino_button, 3, 0, 1, 4)

        self.groupBox = QGroupBox(PersonalWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listView = QListView(self.groupBox)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout.addWidget(self.listView)


        self.gridLayout_8.addWidget(self.groupBox, 7, 0, 1, 4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.alterar_treino_button = QPushButton(PersonalWindow)
        self.alterar_treino_button.setObjectName(u"alterar_treino_button")

        self.gridLayout_8.addWidget(self.alterar_treino_button, 5, 0, 1, 4)

        self.programa_button = QPushButton(PersonalWindow)
        self.programa_button.setObjectName(u"programa_button")

        self.gridLayout_8.addWidget(self.programa_button, 4, 0, 1, 4)

        self.cad_exercicio_button = QPushButton(PersonalWindow)
        self.cad_exercicio_button.setObjectName(u"cad_exercicio_button")

        self.gridLayout_8.addWidget(self.cad_exercicio_button, 6, 0, 1, 3)


        self.gridLayout_3.addLayout(self.gridLayout_8, 0, 2, 1, 1)


        self.retranslateUi(PersonalWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PersonalWindow)
    # setupUi

    def retranslateUi(self, PersonalWindow):
        PersonalWindow.setWindowTitle(QCoreApplication.translate("PersonalWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PersonalWindow", u"Solicita\u00e7\u00f5es", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("PersonalWindow", u"Pendentes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("PersonalWindow", u"Respondidas", None))
        self.cadastrar_button.setText(QCoreApplication.translate("PersonalWindow", u"Cadastrar Usu\u00e1rio", None))
        self.logout_button.setText(QCoreApplication.translate("PersonalWindow", u"logout", None))
        self.configurar_treino_button.setText(QCoreApplication.translate("PersonalWindow", u"Configurar Treino", None))
        self.groupBox.setTitle(QCoreApplication.translate("PersonalWindow", u"Meus Usu\u00e1rios", None))
        self.alterar_treino_button.setText(QCoreApplication.translate("PersonalWindow", u"Alterar Treino", None))
        self.programa_button.setText(QCoreApplication.translate("PersonalWindow", u"Criar Programa", None))
        self.cad_exercicio_button.setText(QCoreApplication.translate("PersonalWindow", u"Cadastrar Excerc\u00edcio", None))
    # retranslateUi

