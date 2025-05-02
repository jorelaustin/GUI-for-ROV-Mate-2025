# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_RobotDashboard(object):
    def setupUi(self, RobotDashboard):
        if not RobotDashboard.objectName():
            RobotDashboard.setObjectName(u"RobotDashboard")
        RobotDashboard.resize(793, 593)
        RobotDashboard.setMinimumSize(QSize(793, 593))
        self.actionOpen_File = QAction(RobotDashboard)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionQuit = QAction(RobotDashboard)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(RobotDashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 793, 561))
        self.tabWidget.setMinimumSize(QSize(793, 561))
        self.VideoFeed = QWidget()
        self.VideoFeed.setObjectName(u"VideoFeed")
        self.CameraMenu = QWidget(self.VideoFeed)
        self.CameraMenu.setObjectName(u"CameraMenu")
        self.CameraMenu.setGeometry(QRect(0, 430, 791, 111))
        self.CameraMenu.setStyleSheet(u"background-color: gray;")
        self.CameraBox = QComboBox(self.CameraMenu)
        self.CameraBox.setObjectName(u"CameraBox")
        self.CameraBox.setGeometry(QRect(360, 31, 141, 31))
        self.CameraBox.setStyleSheet(u"background-color: white;")
        self.Camera = QPushButton(self.CameraMenu)
        self.Camera.setObjectName(u"Camera")
        self.Camera.setGeometry(QRect(260, 31, 81, 31))
        self.Camera.setStyleSheet(u"background-color: white;")
        self.tabWidget.addTab(self.VideoFeed, "")
        self.Graphs = QWidget()
        self.Graphs.setObjectName(u"Graphs")
        self.RecordMenu = QWidget(self.Graphs)
        self.RecordMenu.setObjectName(u"RecordMenu")
        self.RecordMenu.setGeometry(QRect(0, 430, 791, 111))
        self.RecordMenu.setStyleSheet(u"background-color: grey;")
        self.attachFileJSON = QPushButton(self.RecordMenu)
        self.attachFileJSON.setObjectName(u"attachFileJSON")
        self.attachFileJSON.setGeometry(QRect(350, 30, 75, 31))
        self.attachFileJSON.setStyleSheet(u"background-color: white;")
        self.tabWidget.addTab(self.Graphs, "")
        self.Maps = QWidget()
        self.Maps.setObjectName(u"Maps")
        self.RecordMenu_2 = QWidget(self.Maps)
        self.RecordMenu_2.setObjectName(u"RecordMenu_2")
        self.RecordMenu_2.setGeometry(QRect(0, 430, 791, 111))
        self.RecordMenu_2.setStyleSheet(u"background-color: grey;")
        self.attachFileCSV = QPushButton(self.RecordMenu_2)
        self.attachFileCSV.setObjectName(u"attachFileCSV")
        self.attachFileCSV.setGeometry(QRect(350, 30, 75, 31))
        self.attachFileCSV.setStyleSheet(u"background-color: white;")
        self.tabWidget.addTab(self.Maps, "")
        RobotDashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RobotDashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 36))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        RobotDashboard.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(RobotDashboard)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(RobotDashboard)
    # setupUi

    def retranslateUi(self, RobotDashboard):
        RobotDashboard.setWindowTitle(QCoreApplication.translate("RobotDashboard", u"Underwater Robot Dashboard", None))
        self.actionOpen_File.setText(QCoreApplication.translate("RobotDashboard", u"Open...", None))
        self.actionQuit.setText(QCoreApplication.translate("RobotDashboard", u"Quit", None))
        self.Camera.setText(QCoreApplication.translate("RobotDashboard", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VideoFeed), QCoreApplication.translate("RobotDashboard", u"Video Feed", None))
        self.attachFileJSON.setText(QCoreApplication.translate("RobotDashboard", u"Attach File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Graphs), QCoreApplication.translate("RobotDashboard", u"Data", None))
        self.attachFileCSV.setText(QCoreApplication.translate("RobotDashboard", u"Attach File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Maps), QCoreApplication.translate("RobotDashboard", u"Carp Regions", None))
        self.menuFile.setTitle(QCoreApplication.translate("RobotDashboard", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("RobotDashboard", u"Settings", None))
    # retranslateUi

