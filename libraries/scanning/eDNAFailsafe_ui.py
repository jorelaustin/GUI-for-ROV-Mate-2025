# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eDNAFailsafe.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(616, 490)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.finishButton = QPushButton(Widget)
        self.finishButton.setObjectName(u"finishButton")

        self.gridLayout.addWidget(self.finishButton, 1, 1, 1, 1)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 18px;")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.eDNAInput = QPlainTextEdit(Widget)
        self.eDNAInput.setObjectName(u"eDNAInput")
        self.eDNAInput.setStyleSheet(u"background-color: rgb(61, 62, 62)")

        self.gridLayout.addWidget(self.eDNAInput, 0, 1, 1, 1)

        self.sampleDisplay = QLabel(Widget)
        self.sampleDisplay.setObjectName(u"sampleDisplay")
        self.sampleDisplay.setStyleSheet(u"")

        self.gridLayout.addWidget(self.sampleDisplay, 2, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"eDNA Scanner", None))
        self.finishButton.setText(QCoreApplication.translate("Widget", u"Finish", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Input DNA Sequence: ", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Sample:", None))
        self.sampleDisplay.setText("")
    # retranslateUi

