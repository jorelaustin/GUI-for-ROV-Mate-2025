import sys
from PySide6.QtGui import QAction, QFont, QFontDatabase, QKeyEvent
from PySide6.QtCore import QCoreApplication, QFile, Qt, QTimer
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStackedWidget, QLabel, QComboBox, QWidget, QVBoxLayout
)
from PySide6.QtUiTools import QUiLoader

from libaries.visual.visualEffects import STYLE
from libaries.window.fileDialog import FILE_SELECTOR
from libaries.visual.entryViewer import ENTRY_WIDGET
from libaries.camera.cameras import CAMERAS

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file dynamically
        loader = QUiLoader()
        file = QFile("ui/main4.1-test.ui")  # Path to your UI file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)  # Loads in "main.ui" 
        self.setCentralWidget(self.ui)
        self.setWindowTitle("ROV Dashboard")  

        # Grabbing miscellaneous buttons
        self.action_quit = self.ui.findChild(QAction, "actionQuit") # Quit action

        # Connect the QAction "actionQuit" to quit the application
        self.action_quit.triggered.connect(self.safe_quit)  # Quit the application

        # Open up on first tab
        self.stacked_widget = self.ui.findChild(QStackedWidget, "stackedWidget") # stacked widget
        self.stacked_widget.setCurrentIndex(0) 

        # Grabbing buttons for switching tabs
        self.controlPanelButton = self.ui.findChild(QPushButton, "controlPanelButton")
        self.shipwreckButton = self.ui.findChild(QPushButton, "shipwreckButton")
        self.eDNAButton = self.ui.findChild(QPushButton, "eDNAButton")
        self.mappingButton = self.ui.findChild(QPushButton, "mappingButton")
        self.floatButton = self.ui.findChild(QPushButton, "floatButton")

        # Switching tabs
        self.controlPanelButton.clicked.connect(lambda: self.switchTabs(0))
        self.shipwreckButton.clicked.connect(lambda: self.switchTabs(1))
        self.eDNAButton.clicked.connect(lambda: self.switchTabs(2))
        self.mappingButton.clicked.connect(lambda: self.switchTabs(3))
        self.floatButton.clicked.connect(lambda: self.switchTabs(4))

        self.style = STYLE()
        self.style.setStylesheet(QApplication.instance())

        self.controlPanelTab() # Control Panel
        self.floatPanelTab() # Float Panel
        

    def switchTabs(self, tab_index: int):
        # Switch stacked widget
        if 0 <= tab_index < self.stacked_widget.count():
            self.stacked_widget.setCurrentIndex(tab_index)

        # Reset all button styles
        buttons = [self.controlPanelButton, self.shipwreckButton, self.eDNAButton, self.mappingButton, self.floatButton]
        for i, btn in enumerate(buttons):
            if i == tab_index:
                # Active button style
                btn.setStyleSheet("background-color: #007ACC;")  # blue
            else:
                # Inactive button style
                btn.setStyleSheet("background-color: #424242;")  # gray

    # ──────────────────────── CONTROL PANEL PAGE SETUP ────────────────────────
    # Sets up all widgets, signals, and logic related to the Control Panel page.

    def controlPanelTab(self):
        
        # Find object and it's name
        self.program_exit = self.ui.findChild(QPushButton, "program_exit") # Quit action
        # Connect the QAction "actionQuit" to quit the application
        self.program_exit.clicked.connect(self.safe_quit)  # Quit the application

        # Example toggle button in your GUI
        self.secondary_cameras = self.ui.findChild(QWidget, "secondary_camera_feeds")
        self.toggle_view_button = self.ui.findChild(QPushButton, "toggleViewButton")
        self.toggle_view_button.clicked.connect(self.toggle_view_mode)
        self.current_mode = "multi"

        # Dynamically change children once for
        self.cam_1_label = self.ui.findChild(QLabel, "camera_feed_1")
        self.cam_2_label = self.ui.findChild(QLabel, "camera_feed_2")
        self.cam_3_label = self.ui.findChild(QLabel, "camera_feed_3")

        self.cam_1_combo = self.ui.findChild(QComboBox, "camera_feed_1_menu")
        self.cam_2_combo = self.ui.findChild(QComboBox, "camera_feed_2_menu")
        self.cam_3_combo = self.ui.findChild(QComboBox, "camera_feed_3_menu")

        self.cam_1_toggle_btn = self.ui.findChild(QPushButton, "primaryCameraToggleButton")
        self.cam_2_toggle_btn = self.ui.findChild(QPushButton, "secondaryCamera_1_ToggleButton")
        self.cam_3_toggle_btn = self.ui.findChild(QPushButton, "secondaryCamera_2_ToggleButton")

        # Remember to turn off Windows Defender Firewall
        pi_ip = "" 
        # Initialize camera handlers
        self.cameras = CAMERAS(
            labels=[
                self.cam_1_label,
                self.cam_2_label,
                self.cam_3_label
            ],
            combos=[
                self.cam_1_combo,
                self.cam_2_combo,
                self.cam_3_combo
            ],
            toggle_buttons=[
                self.cam_1_toggle_btn,
                self.cam_2_toggle_btn,
                self.cam_3_toggle_btn
            ],
            server_addresses=[
                f"{pi_ip}:5005",
                f"{pi_ip}:5006",
                f"{pi_ip}:5007"
            ]
        )

        # Competition timer display
        self.timerDisplayLabel = self.ui.findChild(QLabel, "timerLabel")
        self.toggleTimerButton = self.ui.findChild(QPushButton, "toggleTimerButton")
        self.resetTimerButton = self.ui.findChild(QPushButton, "resetTimerButton")

        # Toggle and reset timer
        self.toggleTimerButton.clicked.connect(self.toggle_timer)
        self.resetTimerButton.clicked.connect(self.reset_timer)

        # QTimer setup
        self.timer = QTimer()
        self.timer.setInterval(10)  # 10ms = 1/100th of a second
        self.timer.timeout.connect(self.update_label)
        self.elapsed_ms = 0
        self.running = False

    # Safely exits the program
    def safe_quit(self):
        self.close()

    def closeEvent(self, event):
        self.cameras.release_captures()
        super().closeEvent(event)

    # Ability to switch views on Primary Camera
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.showMaximized()
        elif event.key() == Qt.Key_1:
            self.cameras.switch_primary_camera_to(0)
        elif event.key() == Qt.Key_2:
            self.cameras.switch_primary_camera_to(1)
        elif event.key() == Qt.Key_3:
            self.cameras.switch_primary_camera_to(2)

    def toggle_timer(self):
        if self.running:
            self.timer.stop()
            self.toggleTimerButton.setText("Start")
            self.toggleTimerButton.setStyleSheet("background-color: green; color: white")
        else:
            self.timer.start()
            self.toggleTimerButton.setText("Stop")
            self.toggleTimerButton.setStyleSheet("background-color: red; color: white")
        self.running = not self.running

    def reset_timer(self):
        if not self.running:
            self.elapsed_ms = 0
            self.timerDisplayLabel.setText("00:00:00")

    def update_label(self):
        self.elapsed_ms += 10
        minutes = self.elapsed_ms // 60000
        seconds = (self.elapsed_ms % 60000) // 1000
        hundredths = (self.elapsed_ms % 1000) // 10
        self.timerDisplayLabel.setText(f"{minutes:02d}:{seconds:02d}:{hundredths:02d}") 

    # FIXME: Toggles between different camera view modes:
    # - "Multi": All three cameras visible, primary feed enlarged.
    # - "Primary": Only the primary camera is displayed.
    # - "Multi-2": All three camera feeds shown with equal size.

    def toggle_view_mode(self):
            camera_panel_container = self.ui.findChild(QWidget, "control_panel_camera_widget")
            layout = camera_panel_container.layout()

            if self.current_mode == "multi":
                self.cameras.set_primary_only_view(camera_index=0)
                self.secondary_cameras.hide()
                layout.setRowStretch(0, 0)  # Top row
                layout.setRowStretch(1, 1)  # Second row
                self.current_mode = "primary"
            else:
                self.cameras.set_three_camera_view()
                self.secondary_cameras.show()
                layout.setRowStretch(0, 1)  # Top row
                layout.setRowStretch(1, 0)  # Second row
                self.current_mode = "multi"

            # ⏩ Force layout recalculation
            camera_panel_container.updateGeometry()
            camera_panel_container.update()
            camera_panel_container.repaint()

    # ──────────────────────── FLOAT PANEL PAGE SETUP ────────────────────────
    # Sets up all widgets, signals, and logic related to the Float Panel page.
    def floatPanelTab(self):

        # Attach file button
        self.attachFileFloatButton = self.ui.findChild(QPushButton, "attachFileFloat")
        # Connect the QPushButton "attachFile" to open up file dialog
        self.attachFileFloatButton.clicked.connect(self.open_file_dialog)

        # Refresh button
        self.refreshButton = self.ui.findChild(QPushButton, "refreshButton")
        # Connect the QPushButton "attachFile" to open up file dialog
        self.refreshButton.clicked.connect(self.refresh_entries)

        self.entryContainer = self.ui.findChild(QWidget, "database_display")

        self.refresh_entries()

    def refresh_entries(self):
        # Reload entries
        ENTRY_WIDGET.load_entries_into(self.entryContainer, "database/drone_data.db")

    def open_file_dialog(self):
        self.dialog = FILE_SELECTOR(self)
        self.dialog.finished.connect(self.refresh_entries) # auto-refresh
        self.dialog.show()
        


# Function to activate program
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