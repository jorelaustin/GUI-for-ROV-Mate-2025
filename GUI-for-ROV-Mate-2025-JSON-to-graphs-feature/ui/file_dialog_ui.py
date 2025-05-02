# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(490, 600)
        MainWindow.setMinimumSize(QSize(490, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(490, 600))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(9, 10, 470, 150))
        self.tableWidget.setMinimumSize(QSize(470, 150))
        self.canvasPlaceholder = QWidget(self.centralwidget)
        self.canvasPlaceholder.setObjectName(u"canvasPlaceholder")
        self.canvasPlaceholder.setGeometry(QRect(10, 200, 470, 392))
        self.canvasPlaceholder.setMinimumSize(QSize(470, 390))
        self.canvasPlaceholder.setStyleSheet(u"background-color: #3498db;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 172, 251, 23))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.yAxisComboBox = QComboBox(self.layoutWidget)
        self.yAxisComboBox.setObjectName(u"yAxisComboBox")

        self.gridLayout.addWidget(self.yAxisComboBox, 0, 3, 1, 1)

        self.xAxisLabel = QLabel(self.layoutWidget)
        self.xAxisLabel.setObjectName(u"xAxisLabel")
        self.xAxisLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.xAxisLabel, 0, 0, 1, 1)

        self.yAxisLabel = QLabel(self.layoutWidget)
        self.yAxisLabel.setObjectName(u"yAxisLabel")
        self.yAxisLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.yAxisLabel, 0, 2, 1, 1)

        self.xAxisComboBox = QComboBox(self.layoutWidget)
        self.xAxisComboBox.setObjectName(u"xAxisComboBox")

        self.gridLayout.addWidget(self.xAxisComboBox, 0, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(310, 170, 171, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.plotButton = QPushButton(self.layoutWidget1)
        self.plotButton.setObjectName(u"plotButton")

        self.horizontalLayout.addWidget(self.plotButton)

        self.saveFilesButton = QPushButton(self.layoutWidget1)
        self.saveFilesButton.setObjectName(u"saveFilesButton")

        self.horizontalLayout.addWidget(self.saveFilesButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.xAxisLabel.setText(QCoreApplication.translate("MainWindow", u"X-Axis", None))
        self.yAxisLabel.setText(QCoreApplication.translate("MainWindow", u"Y-Axis", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot Graph", None))
        self.saveFilesButton.setText(QCoreApplication.translate("MainWindow", u"Save Files", None))
    # retranslateUi

