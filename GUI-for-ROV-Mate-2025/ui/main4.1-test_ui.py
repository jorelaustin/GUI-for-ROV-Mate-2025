# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main4.1-test.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 797)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buttonsPanel = QWidget(self.centralwidget)
        self.buttonsPanel.setObjectName(u"buttonsPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonsPanel.sizePolicy().hasHeightForWidth())
        self.buttonsPanel.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.buttonsPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(334, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.controlPanelButton = QPushButton(self.buttonsPanel)
        self.controlPanelButton.setObjectName(u"controlPanelButton")
        self.controlPanelButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.controlPanelButton.sizePolicy().hasHeightForWidth())
        self.controlPanelButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.controlPanelButton)

        self.shipwreckButton = QPushButton(self.buttonsPanel)
        self.shipwreckButton.setObjectName(u"shipwreckButton")

        self.horizontalLayout.addWidget(self.shipwreckButton)

        self.eDNAButton = QPushButton(self.buttonsPanel)
        self.eDNAButton.setObjectName(u"eDNAButton")

        self.horizontalLayout.addWidget(self.eDNAButton)

        self.mappingButton = QPushButton(self.buttonsPanel)
        self.mappingButton.setObjectName(u"mappingButton")

        self.horizontalLayout.addWidget(self.mappingButton)

        self.floatButton = QPushButton(self.buttonsPanel)
        self.floatButton.setObjectName(u"floatButton")

        self.horizontalLayout.addWidget(self.floatButton)

        self.horizontalSpacer_3 = QSpacerItem(336, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_4.addWidget(self.buttonsPanel, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.control_panel_page = QWidget()
        self.control_panel_page.setObjectName(u"control_panel_page")
        sizePolicy.setHeightForWidth(self.control_panel_page.sizePolicy().hasHeightForWidth())
        self.control_panel_page.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.control_panel_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.control_panel_tab = QWidget(self.control_panel_page)
        self.control_panel_tab.setObjectName(u"control_panel_tab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.control_panel_tab.sizePolicy().hasHeightForWidth())
        self.control_panel_tab.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.control_panel_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.control_panel_camera_widget = QWidget(self.control_panel_tab)
        self.control_panel_camera_widget.setObjectName(u"control_panel_camera_widget")
        self.control_panel_camera_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.control_panel_camera_widget.sizePolicy().hasHeightForWidth())
        self.control_panel_camera_widget.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.control_panel_camera_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.secondary_camera_feeds = QWidget(self.control_panel_camera_widget)
        self.secondary_camera_feeds.setObjectName(u"secondary_camera_feeds")
        sizePolicy1.setHeightForWidth(self.secondary_camera_feeds.sizePolicy().hasHeightForWidth())
        self.secondary_camera_feeds.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.secondary_camera_feeds)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.camera_feeds = QGridLayout()
        self.camera_feeds.setObjectName(u"camera_feeds")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.camera_feeds.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.camera_feeds.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.camera_feed_2 = QLabel(self.secondary_camera_feeds)
        self.camera_feed_2.setObjectName(u"camera_feed_2")
        sizePolicy.setHeightForWidth(self.camera_feed_2.sizePolicy().hasHeightForWidth())
        self.camera_feed_2.setSizePolicy(sizePolicy)
        self.camera_feed_2.setFrameShape(QFrame.Shape.NoFrame)
        self.camera_feed_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.camera_feeds.addWidget(self.camera_feed_2, 0, 1, 1, 1)

        self.camera_feed_3 = QLabel(self.secondary_camera_feeds)
        self.camera_feed_3.setObjectName(u"camera_feed_3")
        sizePolicy.setHeightForWidth(self.camera_feed_3.sizePolicy().hasHeightForWidth())
        self.camera_feed_3.setSizePolicy(sizePolicy)
        self.camera_feed_3.setFrameShape(QFrame.Shape.NoFrame)
        self.camera_feed_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.camera_feeds.addWidget(self.camera_feed_3, 0, 2, 1, 1)

        self.camera_feeds.setColumnStretch(0, 20)
        self.camera_feeds.setColumnStretch(1, 20)
        self.camera_feeds.setColumnStretch(2, 20)
        self.camera_feeds.setColumnStretch(3, 20)

        self.gridLayout_2.addLayout(self.camera_feeds, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.secondary_camera_feeds, 0, 0, 1, 1)

        self.primary_camera_feed = QWidget(self.control_panel_camera_widget)
        self.primary_camera_feed.setObjectName(u"primary_camera_feed")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.primary_camera_feed.sizePolicy().hasHeightForWidth())
        self.primary_camera_feed.setSizePolicy(sizePolicy4)
        self.gridLayout_15 = QGridLayout(self.primary_camera_feed)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.camera_feed_1 = QLabel(self.primary_camera_feed)
        self.camera_feed_1.setObjectName(u"camera_feed_1")
        sizePolicy.setHeightForWidth(self.camera_feed_1.sizePolicy().hasHeightForWidth())
        self.camera_feed_1.setSizePolicy(sizePolicy)
        self.camera_feed_1.setFrameShape(QFrame.Shape.NoFrame)
        self.camera_feed_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_15.addWidget(self.camera_feed_1, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.primary_camera_feed, 1, 0, 1, 1)

        self.gridLayout_24.setRowStretch(0, 20)
        self.gridLayout_24.setRowStretch(1, 80)

        self.gridLayout_6.addLayout(self.gridLayout_24, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.control_panel_camera_widget)

        self.control_panel_functions_widget = QWidget(self.control_panel_tab)
        self.control_panel_functions_widget.setObjectName(u"control_panel_functions_widget")
        self.gridLayout_5 = QGridLayout(self.control_panel_functions_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.control_panel_scroll = QScrollArea(self.control_panel_functions_widget)
        self.control_panel_scroll.setObjectName(u"control_panel_scroll")
        self.control_panel_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.control_panel_scroll.setLineWidth(0)
        self.control_panel_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.control_panel_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 319, 590))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_box_comms_connect = QGroupBox(self.scrollAreaWidgetContents_3)
        self.group_box_comms_connect.setObjectName(u"group_box_comms_connect")
        self.group_box_comms_connect.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.group_box_comms_connect)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.controller_label = QLabel(self.group_box_comms_connect)
        self.controller_label.setObjectName(u"controller_label")
        self.controller_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.controller_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.controller_label, 0, 0, 1, 1)

        self.tether_counter_label = QLabel(self.group_box_comms_connect)
        self.tether_counter_label.setObjectName(u"tether_counter_label")
        self.tether_counter_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_8.addWidget(self.tether_counter_label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.control_controller_connect = QPushButton(self.group_box_comms_connect)
        self.control_controller_connect.setObjectName(u"control_controller_connect")
        sizePolicy1.setHeightForWidth(self.control_controller_connect.sizePolicy().hasHeightForWidth())
        self.control_controller_connect.setSizePolicy(sizePolicy1)
        self.control_controller_connect.setMinimumSize(QSize(0, 0))
        self.control_controller_connect.setCheckable(True)

        self.gridLayout_8.addWidget(self.control_controller_connect, 0, 1, 1, 1)

        self.label_9 = QLabel(self.group_box_comms_connect)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_8.addWidget(self.label_9, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.control_tether_connect = QPushButton(self.group_box_comms_connect)
        self.control_tether_connect.setObjectName(u"control_tether_connect")

        self.gridLayout_8.addWidget(self.control_tether_connect, 1, 1, 1, 1)

        self.control_pH_connect = QPushButton(self.group_box_comms_connect)
        self.control_pH_connect.setObjectName(u"control_pH_connect")

        self.gridLayout_8.addWidget(self.control_pH_connect, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.group_box_comms_connect)

        self.digital_cameras_menu = QGroupBox(self.scrollAreaWidgetContents_3)
        self.digital_cameras_menu.setObjectName(u"digital_cameras_menu")
        self.digital_cameras_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout = QGridLayout(self.digital_cameras_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toggleViewButton = QPushButton(self.digital_cameras_menu)
        self.toggleViewButton.setObjectName(u"toggleViewButton")

        self.gridLayout.addWidget(self.toggleViewButton, 4, 0, 1, 1)

        self.camera_controls = QWidget(self.digital_cameras_menu)
        self.camera_controls.setObjectName(u"camera_controls")
        self.gridLayout_7 = QGridLayout(self.camera_controls)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.secondaryCamera_2_ToggleButton = QPushButton(self.camera_controls)
        self.secondaryCamera_2_ToggleButton.setObjectName(u"secondaryCamera_2_ToggleButton")

        self.gridLayout_7.addWidget(self.secondaryCamera_2_ToggleButton, 2, 0, 1, 1)

        self.primaryCameraToggleButton = QPushButton(self.camera_controls)
        self.primaryCameraToggleButton.setObjectName(u"primaryCameraToggleButton")

        self.gridLayout_7.addWidget(self.primaryCameraToggleButton, 0, 0, 1, 1)

        self.secondaryCamera_1_ToggleButton = QPushButton(self.camera_controls)
        self.secondaryCamera_1_ToggleButton.setObjectName(u"secondaryCamera_1_ToggleButton")

        self.gridLayout_7.addWidget(self.secondaryCamera_1_ToggleButton, 1, 0, 1, 1)

        self.camera_feed_1_menu = QComboBox(self.camera_controls)
        self.camera_feed_1_menu.setObjectName(u"camera_feed_1_menu")
        self.camera_feed_1_menu.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_7.addWidget(self.camera_feed_1_menu, 0, 1, 1, 1)

        self.camera_feed_2_menu = QComboBox(self.camera_controls)
        self.camera_feed_2_menu.setObjectName(u"camera_feed_2_menu")
        self.camera_feed_2_menu.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_7.addWidget(self.camera_feed_2_menu, 1, 1, 1, 1)

        self.camera_feed_3_menu = QComboBox(self.camera_controls)
        self.camera_feed_3_menu.setObjectName(u"camera_feed_3_menu")
        self.camera_feed_3_menu.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_7.addWidget(self.camera_feed_3_menu, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.camera_controls, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.digital_cameras_menu)

        self.sensor_control = QGroupBox(self.scrollAreaWidgetContents_3)
        self.sensor_control.setObjectName(u"sensor_control")
        self.sensor_control.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_18 = QGridLayout(self.sensor_control)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tetherDisplay = QLabel(self.sensor_control)
        self.tetherDisplay.setObjectName(u"tetherDisplay")
        self.tetherDisplay.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_18.addWidget(self.tetherDisplay, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.phDisplay = QLabel(self.sensor_control)
        self.phDisplay.setObjectName(u"phDisplay")
        self.phDisplay.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_18.addWidget(self.phDisplay, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.sensor_control)

        self.timer_control = QGroupBox(self.scrollAreaWidgetContents_3)
        self.timer_control.setObjectName(u"timer_control")
        self.timer_control.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.timer_control)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.timerLabel = QLabel(self.timer_control)
        self.timerLabel.setObjectName(u"timerLabel")
        self.timerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.timerLabel)

        self.timer_buttons_menu = QWidget(self.timer_control)
        self.timer_buttons_menu.setObjectName(u"timer_buttons_menu")
        self.gridLayout_21 = QGridLayout(self.timer_buttons_menu)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.resetTimerButton = QPushButton(self.timer_buttons_menu)
        self.resetTimerButton.setObjectName(u"resetTimerButton")

        self.gridLayout_21.addWidget(self.resetTimerButton, 0, 0, 1, 1)

        self.toggleTimerButton = QPushButton(self.timer_buttons_menu)
        self.toggleTimerButton.setObjectName(u"toggleTimerButton")

        self.gridLayout_21.addWidget(self.toggleTimerButton, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.timer_buttons_menu)


        self.verticalLayout.addWidget(self.timer_control)


        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.control_panel_scroll.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_5.addWidget(self.control_panel_scroll, 0, 1, 1, 1)

        self.CreditWidget = QHBoxLayout()
        self.CreditWidget.setObjectName(u"CreditWidget")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CreditWidget.addItem(self.horizontalSpacer_8)

        self.label_14 = QLabel(self.control_panel_functions_widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.CreditWidget.addWidget(self.label_14)

        self.program_exit = QPushButton(self.control_panel_functions_widget)
        self.program_exit.setObjectName(u"program_exit")

        self.CreditWidget.addWidget(self.program_exit)


        self.gridLayout_5.addLayout(self.CreditWidget, 1, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.control_panel_functions_widget)

        self.horizontalLayout_3.setStretch(0, 95)
        self.horizontalLayout_3.setStretch(1, 5)

        self.gridLayout_3.addWidget(self.control_panel_tab, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.control_panel_page)
        self.shipwreck_panel_page = QWidget()
        self.shipwreck_panel_page.setObjectName(u"shipwreck_panel_page")
        self.gridLayout_9 = QGridLayout(self.shipwreck_panel_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.shipwreck_panel = QWidget(self.shipwreck_panel_page)
        self.shipwreck_panel.setObjectName(u"shipwreck_panel")
        self.horizontalLayout_7 = QHBoxLayout(self.shipwreck_panel)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.shipwreck_gui_panel = QWidget(self.shipwreck_panel)
        self.shipwreck_gui_panel.setObjectName(u"shipwreck_gui_panel")
        self.verticalLayout_5 = QVBoxLayout(self.shipwreck_gui_panel)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.shipwreck_identifer = QGroupBox(self.shipwreck_gui_panel)
        self.shipwreck_identifer.setObjectName(u"shipwreck_identifer")
        self.shipwreck_identifer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.shipwreck_identifer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.shipwreck_combo_boxes_menu = QWidget(self.shipwreck_identifer)
        self.shipwreck_combo_boxes_menu.setObjectName(u"shipwreck_combo_boxes_menu")
        self.gridLayout_22 = QGridLayout(self.shipwreck_combo_boxes_menu)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label = QLabel(self.shipwreck_combo_boxes_menu)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.label, 0, 0, 1, 1)

        self.shipType_menu = QComboBox(self.shipwreck_combo_boxes_menu)
        self.shipType_menu.setObjectName(u"shipType_menu")

        self.gridLayout_22.addWidget(self.shipType_menu, 0, 1, 1, 1)

        self.label_2 = QLabel(self.shipwreck_combo_boxes_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.label_2, 1, 0, 1, 1)

        self.shipLength_menu = QComboBox(self.shipwreck_combo_boxes_menu)
        self.shipLength_menu.setObjectName(u"shipLength_menu")

        self.gridLayout_22.addWidget(self.shipLength_menu, 1, 1, 1, 1)

        self.label_3 = QLabel(self.shipwreck_combo_boxes_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.label_3, 2, 0, 1, 1)

        self.shipCargo_menu = QComboBox(self.shipwreck_combo_boxes_menu)
        self.shipCargo_menu.setObjectName(u"shipCargo_menu")

        self.gridLayout_22.addWidget(self.shipCargo_menu, 2, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.shipwreck_combo_boxes_menu)

        self.shipwreck_buttons_menu = QWidget(self.shipwreck_identifer)
        self.shipwreck_buttons_menu.setObjectName(u"shipwreck_buttons_menu")
        self.verticalLayout_7 = QVBoxLayout(self.shipwreck_buttons_menu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.shipFinishButton = QPushButton(self.shipwreck_buttons_menu)
        self.shipFinishButton.setObjectName(u"shipFinishButton")

        self.verticalLayout_7.addWidget(self.shipFinishButton)

        self.attachFileShipwreck = QPushButton(self.shipwreck_buttons_menu)
        self.attachFileShipwreck.setObjectName(u"attachFileShipwreck")

        self.verticalLayout_7.addWidget(self.attachFileShipwreck)


        self.verticalLayout_6.addWidget(self.shipwreck_buttons_menu)

        self.verticalLayout_6.setStretch(0, 80)
        self.verticalLayout_6.setStretch(1, 20)

        self.verticalLayout_5.addWidget(self.shipwreck_identifer)

        self.shipwreck_name_result = QGroupBox(self.shipwreck_gui_panel)
        self.shipwreck_name_result.setObjectName(u"shipwreck_name_result")
        self.shipwreck_name_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.shipwreck_name_result)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.shipNameDisplay = QLabel(self.shipwreck_name_result)
        self.shipNameDisplay.setObjectName(u"shipNameDisplay")
        self.shipNameDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.shipNameDisplay)

        self.shipwreckResetButton = QPushButton(self.shipwreck_name_result)
        self.shipwreckResetButton.setObjectName(u"shipwreckResetButton")

        self.verticalLayout_8.addWidget(self.shipwreckResetButton)


        self.verticalLayout_5.addWidget(self.shipwreck_name_result)

        self.verticalLayout_5.setStretch(0, 50)
        self.verticalLayout_5.setStretch(1, 50)

        self.horizontalLayout_7.addWidget(self.shipwreck_gui_panel)

        self.shipwreck_image_result_panel = QWidget(self.shipwreck_panel)
        self.shipwreck_image_result_panel.setObjectName(u"shipwreck_image_result_panel")
        self.gridLayout_23 = QGridLayout(self.shipwreck_image_result_panel)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.shipwreckImageLabel = QLabel(self.shipwreck_image_result_panel)
        self.shipwreckImageLabel.setObjectName(u"shipwreckImageLabel")
        self.shipwreckImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.shipwreckImageLabel, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.shipwreck_image_result_panel)

        self.horizontalLayout_7.setStretch(0, 30)
        self.horizontalLayout_7.setStretch(1, 70)

        self.gridLayout_9.addWidget(self.shipwreck_panel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.shipwreck_panel_page)
        self.eDNA_panel_page = QWidget()
        self.eDNA_panel_page.setObjectName(u"eDNA_panel_page")
        self.gridLayout_12 = QGridLayout(self.eDNA_panel_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.eDNA_panel_page_tab = QWidget(self.eDNA_panel_page)
        self.eDNA_panel_page_tab.setObjectName(u"eDNA_panel_page_tab")
        self.verticalLayout_2 = QVBoxLayout(self.eDNA_panel_page_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.eDNA_button_panel = QWidget(self.eDNA_panel_page_tab)
        self.eDNA_button_panel.setObjectName(u"eDNA_button_panel")
        self.horizontalLayout_4 = QHBoxLayout(self.eDNA_button_panel)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.eDNA_button_panel_groupbox = QGroupBox(self.eDNA_button_panel)
        self.eDNA_button_panel_groupbox.setObjectName(u"eDNA_button_panel_groupbox")
        self.horizontalLayout_10 = QHBoxLayout(self.eDNA_button_panel_groupbox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.attachFileEDNA = QPushButton(self.eDNA_button_panel_groupbox)
        self.attachFileEDNA.setObjectName(u"attachFileEDNA")

        self.horizontalLayout_10.addWidget(self.attachFileEDNA)

        self.eDNAFailsafeButton = QPushButton(self.eDNA_button_panel_groupbox)
        self.eDNAFailsafeButton.setObjectName(u"eDNAFailsafeButton")

        self.horizontalLayout_10.addWidget(self.eDNAFailsafeButton)

        self.eDNAClearResultsButton = QPushButton(self.eDNA_button_panel_groupbox)
        self.eDNAClearResultsButton.setObjectName(u"eDNAClearResultsButton")

        self.horizontalLayout_10.addWidget(self.eDNAClearResultsButton)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_10.setStretch(0, 8)
        self.horizontalLayout_10.setStretch(1, 8)
        self.horizontalLayout_10.setStretch(2, 8)
        self.horizontalLayout_10.setStretch(3, 74)

        self.horizontalLayout_4.addWidget(self.eDNA_button_panel_groupbox)


        self.verticalLayout_2.addWidget(self.eDNA_button_panel)

        self.eDNA_samples_panel = QWidget(self.eDNA_panel_page_tab)
        self.eDNA_samples_panel.setObjectName(u"eDNA_samples_panel")
        self.horizontalLayout_5 = QHBoxLayout(self.eDNA_samples_panel)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.eDNA_samples_panel_groupbox = QGroupBox(self.eDNA_samples_panel)
        self.eDNA_samples_panel_groupbox.setObjectName(u"eDNA_samples_panel_groupbox")
        self.horizontalLayout_9 = QHBoxLayout(self.eDNA_samples_panel_groupbox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_2 = QWidget(self.eDNA_samples_panel_groupbox)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_16 = QGridLayout(self.widget_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_4, 0, 0, 1, 1)

        self.sample1Label = QLabel(self.widget_2)
        self.sample1Label.setObjectName(u"sample1Label")
        self.sample1Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.sample1Label, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_5, 1, 0, 1, 1)

        self.sample2Label = QLabel(self.widget_2)
        self.sample2Label.setObjectName(u"sample2Label")
        self.sample2Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.sample2Label, 1, 1, 1, 1)

        self.sample3Label = QLabel(self.widget_2)
        self.sample3Label.setObjectName(u"sample3Label")
        self.sample3Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.sample3Label, 2, 1, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_7, 4, 0, 1, 1)

        self.sample4Label = QLabel(self.widget_2)
        self.sample4Label.setObjectName(u"sample4Label")
        self.sample4Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.sample4Label, 4, 1, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_8, 5, 0, 1, 1)

        self.sample5Label = QLabel(self.widget_2)
        self.sample5Label.setObjectName(u"sample5Label")
        self.sample5Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.sample5Label, 5, 1, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_6, 2, 0, 1, 1)

        self.gridLayout_16.setColumnStretch(0, 40)
        self.gridLayout_16.setColumnStretch(1, 60)

        self.horizontalLayout_9.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.eDNA_samples_panel_groupbox)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_17 = QGridLayout(self.widget_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_15, 0, 0, 1, 1)

        self.sample6Label = QLabel(self.widget_3)
        self.sample6Label.setObjectName(u"sample6Label")
        self.sample6Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.sample6Label, 0, 1, 1, 1)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_17, 1, 0, 1, 1)

        self.sample7Label = QLabel(self.widget_3)
        self.sample7Label.setObjectName(u"sample7Label")
        self.sample7Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.sample7Label, 1, 1, 1, 1)

        self.label_19 = QLabel(self.widget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_19, 2, 0, 1, 1)

        self.sample8Label = QLabel(self.widget_3)
        self.sample8Label.setObjectName(u"sample8Label")
        self.sample8Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.sample8Label, 2, 1, 1, 1)

        self.label_21 = QLabel(self.widget_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_21, 3, 0, 1, 1)

        self.sample9Label = QLabel(self.widget_3)
        self.sample9Label.setObjectName(u"sample9Label")
        self.sample9Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.sample9Label, 3, 1, 1, 1)

        self.label_22 = QLabel(self.widget_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_22, 4, 0, 1, 1)

        self.sample10Label = QLabel(self.widget_3)
        self.sample10Label.setObjectName(u"sample10Label")
        self.sample10Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.sample10Label, 4, 1, 1, 1)

        self.gridLayout_17.setColumnStretch(0, 40)
        self.gridLayout_17.setColumnStretch(1, 60)

        self.horizontalLayout_9.addWidget(self.widget_3)


        self.horizontalLayout_5.addWidget(self.eDNA_samples_panel_groupbox)


        self.verticalLayout_2.addWidget(self.eDNA_samples_panel)

        self.verticalLayout_2.setStretch(1, 70)

        self.gridLayout_12.addWidget(self.eDNA_panel_page_tab, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.eDNA_panel_page)
        self.mapping_panel_page = QWidget()
        self.mapping_panel_page.setObjectName(u"mapping_panel_page")
        self.gridLayout_13 = QGridLayout(self.mapping_panel_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.mapping_panel = QWidget(self.mapping_panel_page)
        self.mapping_panel.setObjectName(u"mapping_panel")
        self.mapping_panel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_9 = QVBoxLayout(self.mapping_panel)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.mapping_image_widget = QWidget(self.mapping_panel)
        self.mapping_image_widget.setObjectName(u"mapping_image_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.mapping_image_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.mapLabel = QLabel(self.mapping_image_widget)
        self.mapLabel.setObjectName(u"mapLabel")
        self.mapLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.mapLabel.sizePolicy().hasHeightForWidth())
        self.mapLabel.setSizePolicy(sizePolicy)
        self.mapLabel.setMinimumSize(QSize(0, 0))
        self.mapLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.mapLabel)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addWidget(self.mapping_image_widget)

        self.mapping_button_widget = QWidget(self.mapping_panel)
        self.mapping_button_widget.setObjectName(u"mapping_button_widget")
        self.gridLayout_14 = QGridLayout(self.mapping_button_widget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox = QGroupBox(self.mapping_button_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.mappingFailsafeButton = QPushButton(self.groupBox)
        self.mappingFailsafeButton.setObjectName(u"mappingFailsafeButton")

        self.horizontalLayout_2.addWidget(self.mappingFailsafeButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.previous = QPushButton(self.groupBox)
        self.previous.setObjectName(u"previous")

        self.horizontalLayout_2.addWidget(self.previous)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.attachFileMapping = QPushButton(self.groupBox)
        self.attachFileMapping.setObjectName(u"attachFileMapping")

        self.horizontalLayout_2.addWidget(self.attachFileMapping)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.next = QPushButton(self.groupBox)
        self.next.setObjectName(u"next")

        self.horizontalLayout_2.addWidget(self.next)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)

        self.mappingResetButton = QPushButton(self.groupBox)
        self.mappingResetButton.setObjectName(u"mappingResetButton")

        self.horizontalLayout_2.addWidget(self.mappingResetButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_2.setStretch(0, 13)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 4)
        self.horizontalLayout_2.setStretch(3, 10)
        self.horizontalLayout_2.setStretch(4, 4)
        self.horizontalLayout_2.setStretch(5, 10)
        self.horizontalLayout_2.setStretch(6, 4)
        self.horizontalLayout_2.setStretch(7, 10)
        self.horizontalLayout_2.setStretch(8, 4)
        self.horizontalLayout_2.setStretch(9, 10)
        self.horizontalLayout_2.setStretch(10, 13)

        self.gridLayout_14.addWidget(self.groupBox, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.mapping_button_widget)

        self.verticalLayout_9.setStretch(0, 80)
        self.verticalLayout_9.setStretch(1, 20)

        self.gridLayout_13.addWidget(self.mapping_panel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.mapping_panel_page)
        self.float_panel_page = QWidget()
        self.float_panel_page.setObjectName(u"float_panel_page")
        self.gridLayout_11 = QGridLayout(self.float_panel_page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.float_panel_tab = QWidget(self.float_panel_page)
        self.float_panel_tab.setObjectName(u"float_panel_tab")
        self.verticalLayout_3 = QVBoxLayout(self.float_panel_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.float_panel_menu = QWidget(self.float_panel_tab)
        self.float_panel_menu.setObjectName(u"float_panel_menu")
        self.gridLayout_25 = QGridLayout(self.float_panel_menu)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.float_panel_group_box = QGroupBox(self.float_panel_menu)
        self.float_panel_group_box.setObjectName(u"float_panel_group_box")
        self.float_panel_group_box.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_8 = QHBoxLayout(self.float_panel_group_box)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.attachFileFloat = QPushButton(self.float_panel_group_box)
        self.attachFileFloat.setObjectName(u"attachFileFloat")

        self.horizontalLayout_8.addWidget(self.attachFileFloat)

        self.refreshButton = QPushButton(self.float_panel_group_box)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout_8.addWidget(self.refreshButton)

        self.horizontalSpacer_10 = QSpacerItem(417, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_8.setStretch(0, 8)
        self.horizontalLayout_8.setStretch(1, 8)
        self.horizontalLayout_8.setStretch(2, 84)

        self.gridLayout_25.addWidget(self.float_panel_group_box, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.float_panel_menu)

        self.database_display = QWidget(self.float_panel_tab)
        self.database_display.setObjectName(u"database_display")

        self.verticalLayout_3.addWidget(self.database_display)

        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 90)

        self.gridLayout_11.addWidget(self.float_panel_tab, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.float_panel_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 36))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.controlPanelButton.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.shipwreckButton.setText(QCoreApplication.translate("MainWindow", u"Shipwreck", None))
        self.eDNAButton.setText(QCoreApplication.translate("MainWindow", u"eDNA", None))
        self.mappingButton.setText(QCoreApplication.translate("MainWindow", u"Mapping", None))
        self.floatButton.setText(QCoreApplication.translate("MainWindow", u"Float", None))
        self.camera_feed_2.setText("")
        self.camera_feed_3.setText("")
        self.camera_feed_1.setText("")
        self.group_box_comms_connect.setTitle(QCoreApplication.translate("MainWindow", u"Communication Setup", None))
        self.controller_label.setText(QCoreApplication.translate("MainWindow", u"Controller", None))
        self.tether_counter_label.setText(QCoreApplication.translate("MainWindow", u"Tether Counter", None))
        self.control_controller_connect.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"pH Sensor", None))
        self.control_tether_connect.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.control_pH_connect.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.digital_cameras_menu.setTitle(QCoreApplication.translate("MainWindow", u"Cameras", None))
        self.toggleViewButton.setText(QCoreApplication.translate("MainWindow", u"Toggle Camera View", None))
        self.secondaryCamera_2_ToggleButton.setText(QCoreApplication.translate("MainWindow", u"2nd - 2", None))
        self.primaryCameraToggleButton.setText(QCoreApplication.translate("MainWindow", u"1st", None))
        self.secondaryCamera_1_ToggleButton.setText(QCoreApplication.translate("MainWindow", u"2nd - 1", None))
        self.sensor_control.setTitle(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.tetherDisplay.setText(QCoreApplication.translate("MainWindow", u"Tether Out: ---", None))
        self.phDisplay.setText(QCoreApplication.translate("MainWindow", u"pH: ---", None))
        self.timer_control.setTitle(QCoreApplication.translate("MainWindow", u"Competition Time", None))
        self.timerLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.resetTimerButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.toggleTimerButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Developed by Crush Depth Team", None))
        self.program_exit.setText(QCoreApplication.translate("MainWindow", u"Exit Program", None))
        self.shipwreck_identifer.setTitle(QCoreApplication.translate("MainWindow", u"Shipwreck Identifer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ship Type:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ship Length (m):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ship Cargo:", None))
        self.shipFinishButton.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.attachFileShipwreck.setText(QCoreApplication.translate("MainWindow", u"Attach File", None))
        self.shipwreck_name_result.setTitle(QCoreApplication.translate("MainWindow", u"Ship Name", None))
        self.shipNameDisplay.setText("")
        self.shipwreckResetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.shipwreckImageLabel.setText("")
        self.eDNA_button_panel_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"eDNA Controls", None))
        self.attachFileEDNA.setText(QCoreApplication.translate("MainWindow", u"Attach File", None))
        self.eDNAFailsafeButton.setText(QCoreApplication.translate("MainWindow", u"Manual Input", None))
        self.eDNAClearResultsButton.setText(QCoreApplication.translate("MainWindow", u"Clear Results", None))
        self.eDNA_samples_panel_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"eDNA Samples", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 1:", None))
        self.sample1Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 2:", None))
        self.sample2Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.sample3Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 4:", None))
        self.sample4Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 5:", None))
        self.sample5Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 3:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 6:", None))
        self.sample6Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 7:", None))
        self.sample7Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 8:", None))
        self.sample8Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 9:", None))
        self.sample9Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SAMPLE 10:", None))
        self.sample10Label.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.mapLabel.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mapping Controls", None))
        self.mappingFailsafeButton.setText(QCoreApplication.translate("MainWindow", u"Manual Input", None))
        self.previous.setText(QCoreApplication.translate("MainWindow", u"Previous Year", None))
        self.attachFileMapping.setText(QCoreApplication.translate("MainWindow", u"Load CSV", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"Next Year", None))
        self.mappingResetButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.float_panel_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Manage Entries", None))
        self.attachFileFloat.setText(QCoreApplication.translate("MainWindow", u"Attach File", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

