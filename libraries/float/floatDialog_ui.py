# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'floatDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_FloatDialog(object):
    def setupUi(self, FloatDialog):
        if not FloatDialog.objectName():
            FloatDialog.setObjectName(u"FloatDialog")
        FloatDialog.resize(489, 254)
        self.gridLayout = QGridLayout(FloatDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.messageInput = QPlainTextEdit(FloatDialog)
        self.messageInput.setObjectName(u"messageInput")

        self.gridLayout.addWidget(self.messageInput, 0, 0, 1, 1)

        self.floatSend = QPushButton(FloatDialog)
        self.floatSend.setObjectName(u"floatSend")

        self.gridLayout.addWidget(self.floatSend, 1, 0, 1, 1)

        self.floatGo = QPushButton(FloatDialog)
        self.floatGo.setObjectName(u"floatGo")
        self.floatGo.setStyleSheet(u"background-color: green;")

        self.gridLayout.addWidget(self.floatGo, 2, 0, 1, 1)

        self.floatStop = QPushButton(FloatDialog)
        self.floatStop.setObjectName(u"floatStop")
        self.floatStop.setStyleSheet(u"background-color: red;")

        self.gridLayout.addWidget(self.floatStop, 4, 0, 1, 1)

        self.messageReceived = QLabel(FloatDialog)
        self.messageReceived.setObjectName(u"messageReceived")

        self.gridLayout.addWidget(self.messageReceived, 6, 0, 1, 1)

        self.messageSent = QLabel(FloatDialog)
        self.messageSent.setObjectName(u"messageSent")

        self.gridLayout.addWidget(self.messageSent, 5, 0, 1, 1)


        self.retranslateUi(FloatDialog)

        QMetaObject.connectSlotsByName(FloatDialog)
    # setupUi

    def retranslateUi(self, FloatDialog):
        FloatDialog.setWindowTitle(QCoreApplication.translate("FloatDialog", u"FloatDialog", None))
        self.floatSend.setText(QCoreApplication.translate("FloatDialog", u"SEND", None))
        self.floatGo.setText(QCoreApplication.translate("FloatDialog", u"GO", None))
        self.floatStop.setText(QCoreApplication.translate("FloatDialog", u"STOP", None))
        self.messageReceived.setText(QCoreApplication.translate("FloatDialog", u"MESSAGE RECEIVED:", None))
        self.messageSent.setText(QCoreApplication.translate("FloatDialog", u"MESSAGE SENT:", None))
    # retranslateUi

