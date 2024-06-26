# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ExercicioDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_ExercicioDialog(object):
    def setupUi(self, ExercicioDialog):
        if not ExercicioDialog.objectName():
            ExercicioDialog.setObjectName(u"ExercicioDialog")
        ExercicioDialog.resize(636, 497)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExercicioDialog.sizePolicy().hasHeightForWidth())
        ExercicioDialog.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(ExercicioDialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_button = QPushButton(ExercicioDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)

        self.salvar_button = QPushButton(ExercicioDialog)
        self.salvar_button.setObjectName(u"salvar_button")

        self.horizontalLayout.addWidget(self.salvar_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(ExercicioDialog)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(ExercicioDialog)

        QMetaObject.connectSlotsByName(ExercicioDialog)
    # setupUi

    def retranslateUi(self, ExercicioDialog):
        ExercicioDialog.setWindowTitle(QCoreApplication.translate("ExercicioDialog", u"MainWindow", None))
        self.cancel_button.setText(QCoreApplication.translate("ExercicioDialog", u"Cancel", None))
        self.salvar_button.setText(QCoreApplication.translate("ExercicioDialog", u"Salvar", None))
    # retranslateUi

