import sys
from PySide6.QtGui import QAction, QFont, QFontDatabase, QKeyEvent
from PySide6.QtCore import QCoreApplication, QFile, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStackedWidget, QLabel, QComboBox
)
from PySide6.QtUiTools import QUiLoader

from libaries.visual.visualEffects import STYLE

# FOR CAMERAS CLASS
import sys
import cv2
from PySide6.QtCore import QTimer, Qt, QFile
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file dynamically
        loader = QUiLoader()
        file = QFile("ui/main2.ui")  # Path to your UI file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)  # Loads in "main.ui" 
        self.setCentralWidget(self.ui)
        self.setWindowTitle("ROV Dashboard")  

        # Open up on first tab
        self.stacked_widget = self.ui.findChild(QStackedWidget, "stackedWidget") # stacked widget
        self.stacked_widget.setCurrentIndex(0) 

        # Grabbing buttons for switching tabs
        self.controlPanelButton = self.ui.findChild(QPushButton, "controlPanelButton")
        self.dataButton = self.ui.findChild(QPushButton, "dataButton")
        self.mappingButton = self.ui.findChild(QPushButton, "mappingButton")

        # Switching tabs
        self.controlPanelButton.clicked.connect(lambda: self.switchTabs(0))
        self.dataButton.clicked.connect(lambda: self.switchTabs(1))
        self.mappingButton.clicked.connect(lambda: self.switchTabs(2))

        self.style = STYLE()
        self.style.setStylesheet(QApplication.instance())

        self.controlPanelTab() # Control Panel

    def switchTabs(self, tab_index: int):
        # Switch stacked widget
        if 0 <= tab_index < self.stacked_widget.count():
            self.stacked_widget.setCurrentIndex(tab_index)

        # Reset all button styles
        buttons = [self.controlPanelButton, self.dataButton, self.mappingButton]
        for i, btn in enumerate(buttons):
            if i == tab_index:
                # Active button style
                btn.setStyleSheet("background-color: #007ACC;")  # blue
            else:
                # Inactive button style
                btn.setStyleSheet("background-color: #424242;")  # gray


    def controlPanelTab(self):
        # Find object and it's name
        self.program_exit = self.ui.findChild(QPushButton, "program_exit") # Quit action
        # Connect the QAction "actionQuit" to quit the application
        self.program_exit.clicked.connect(QApplication.instance().quit)  # Quit the application

        self.cam_1_label = self.ui.findChild(QLabel, "camera_feed_1")
        self.cam_2_label = self.ui.findChild(QLabel, "camera_feed_2")
        self.cam_3_label = self.ui.findChild(QLabel, "camera_feed_3")
        self.cam_4_label = self.ui.findChild(QLabel, "camera_feed_4")

        self.cam_1_combo = self.ui.findChild(QComboBox, "camera_feed_1_menu")
        self.cam_2_combo = self.ui.findChild(QComboBox, "camera_feed_2_menu")
        self.cam_3_combo = self.ui.findChild(QComboBox, "camera_feed_3_menu")
        self.cam_4_combo = self.ui.findChild(QComboBox, "camera_feed_4_menu")

        self.cam_1_toggle_btn = self.ui.findChild(QPushButton, "primaryCameraToggleButton")
        self.cam_2_toggle_btn = self.ui.findChild(QPushButton, "secondaryCamera_1_ToggleButton")
        self.cam_3_toggle_btn = self.ui.findChild(QPushButton, "secondaryCamera_2_ToggleButton")
        self.cam_4_toggle_btn = self.ui.findChild(QPushButton, "secondaryCamera_3_ToggleButton")

        # Initialize camera handlers
        self.cameras = [
            CAMERA(self.cam_1_label, self.cam_1_combo, self.cam_1_toggle_btn, self),
            CAMERA(self.cam_2_label, self.cam_2_combo, self.cam_2_toggle_btn, self),
            CAMERA(self.cam_3_label, self.cam_3_combo, self.cam_3_toggle_btn, self),
            CAMERA(self.cam_4_label, self.cam_4_combo, self.cam_4_toggle_btn, self),
        ]
    
    def closeEvent(self, event):
        for cam in self.cameras:
            cam.cleanup()
        event.accept()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.showMaximized()  # Press Esc to go to maximized

class CAMERA:
    def __init__(self, label, combo_box, toggle_button, parent=None):
        self.label = label
        self.combo_box = combo_box
        self.toggle_button = toggle_button
        self.capture = None
        self.timer = QTimer(parent)
        self.timer.timeout.connect(self.update_frame)

        self.toggle_button.clicked.connect(self.toggle_camera)
        self.combo_box.addItems([f"Camera {i+1}" for i in range(4)])  # Named cameras

    def toggle_camera(self):
        if self.capture is None:
            cam_text = self.combo_box.currentText()
            cam_index = int(cam_text.split()[-1]) - 1  # Convert "Camera 1" → 0
            
            cap = cv2.VideoCapture(cam_index)
            if cap.isOpened():
                self.capture = cap
                self.toggle_button.setStyleSheet("background-color: #007ACC;") #Turn OFF
                self.timer.start(30)
            else:
                self.label.setText("Camera not found")
        else:
            self.stop_camera()

    def stop_camera(self):
        if self.capture:
            self.timer.stop()
            self.capture.release()
            self.capture = None
            self.label.clear()
            self.label.setStyleSheet("background-color: black;")
            self.toggle_button.setStyleSheet("background-color: #424242;") #Turn ON

    def update_frame(self):
        if self.capture and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Crop frame to 16:9
                h, w, _ = frame.shape
                desired_w = w
                desired_h = int(w * 9 / 16)
                if desired_h > h:
                    desired_h = h
                    desired_w = int(h * 16 / 9)

                y_offset = (h - desired_h) // 2
                x_offset = (w - desired_w) // 2
                frame = frame[y_offset:y_offset + desired_h, x_offset:x_offset + desired_w]

                # Convert to QPixmap
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_img)

                scaled_pixmap = pixmap.scaled(
                    self.label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.label.setPixmap(scaled_pixmap)

    def cleanup(self):
        self.stop_camera()

def guiInitiate(): 
    """
    PURPOSE

    Launches program and selects font.

    INPUTS

    NONE

    RETURNS

    NONE
    """
    # Set the attribute BEFORE creating QApplication
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    # Run the application
    app = QApplication(sys.argv)

    # Load the font file
    font_id = QFontDatabase.addApplicationFont("graphics/fonts/bahnschrift.ttf")

    # Get the font family name
    if font_id != -1:
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(family)
        app.setFont(custom_font)
        print(f"Loaded custom font: {family}")
    else:
        print("Failed to load custom font.")
        
    app.setStyle("Fusion")

    window = MyApp()
    window.showFullScreen() # Show screen
    sys.exit(app.exec())

if __name__ == '__main__':
    guiInitiate()