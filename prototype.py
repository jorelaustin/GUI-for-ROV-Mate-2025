import os
import cv2
import sys
import pandas as pd
from PySide6.QtGui import QAction, QFont, QFontDatabase, QPixmap, QImage, QKeyEvent  
from PySide6.QtCore import QCoreApplication, QFile, Qt, QTimer
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStackedWidget, QLabel,
    QComboBox, QWidget, QFileDialog
)
from PySide6.QtUiTools import QUiLoader

from libraries.visual.visualEffects import STYLE
from libraries.window.fileDialog import FILE_SELECTOR
from libraries.visual.entryViewer import ENTRY_WIDGET
from libraries.camera.cameras_new import CAMERAS
from libraries.shipwreck.shipwreckLogic import SHIPWRECK_LOGIC
from libraries.mapping.modelCarpRegionLogic import CARP_REGION_MODEL
from libraries.scanning.eDNA import EDNA_LOGIC


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file dynamically
        loader = QUiLoader()
        file = QFile("ui/main5.ui")  # Path to your UI file
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
        self.shipwreckPanelTab() # Shipwreck Panel
        self.eDNAPanelTab() # eDNA Identification panel
        self.mappingPanelTab() # Model Carp Regions Panel
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

        # Start in Multi-View
        self.cameras_stacked_widget = self.ui.findChild(QStackedWidget, "camerasStackedWidget")
        self.cameras_stacked_widget.setCurrentIndex(0)
        self.current_mode = "multi"

        # Multi-View
        self.cam_1_label = self.ui.findChild(QLabel, "camera_feed_1")
        self.cam_2_label = self.ui.findChild(QLabel, "camera_feed_2")
        self.cam_3_label = self.ui.findChild(QLabel, "camera_feed_3")

        '''
        # Multi-View-2
        self.cam_4_label = self.ui.findChild(QLabel, "camera_feed_4")
        self.cam_5_label = self.ui.findChild(QLabel, "camera_feed_5")
        self.cam_6_label = self.ui.findChild(QLabel, "camera_feed_6")

        # Multi-View-2
        self.cam_7_label = self.ui.findChild(QLabel, "camera_feed_7")
        '''

        self.cam_1_combo = self.ui.findChild(QComboBox, "camera_feed_1_menu")
        self.cam_2_combo = self.ui.findChild(QComboBox, "camera_feed_2_menu") # Hides on Primary View
        self.cam_3_combo = self.ui.findChild(QComboBox, "camera_feed_3_menu") # Hides on Primary View

        self.cam_1_toggle_btn = self.ui.findChild(QPushButton, "primaryCameraToggleButton")
        self.cam_2_toggle_btn = self.ui.findChild(QPushButton, "secondaryCamera_1_ToggleButton") # Hides on Primary View
        self.cam_3_toggle_btn = self.ui.findChild(QPushButton, "secondaryCamera_2_ToggleButton") # Hides on Primary View

        # Remember to turn off Windows Defender Firewall
        pi_ip = "" 
        ports = [5005, 5006, 5007]
        # Initialize camera handlers
        self.init_camera_multi_view_1(pi_ip, ports)

        # View toggle button
        '''
        self.toggle_view_button = self.ui.findChild(QPushButton, "toggleViewButton")
        self.toggle_view_button.clicked.connect(lambda: self.toggle_view_mode(pi_ip, ports, ports_2))
        self.toggle_view_button.setText("Switch to Multi-2 View")  # First cycle
        '''

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

    # Multi-View-1
    def init_camera_multi_view_1(self, pi_ip, ports):
        server_addresses = [f"{pi_ip}:{port}" for port in ports]

        self.cameras = CAMERAS(
            labels = [self.cam_1_label, self.cam_2_label, self.cam_3_label],
            combos = [self.cam_1_combo, self.cam_2_combo, self.cam_3_combo],
            toggle_buttons = [self.cam_1_toggle_btn, self.cam_2_toggle_btn, self.cam_3_toggle_btn],
            server_addresses = server_addresses
        )

    '''
    # Multi-View-2
    def init_camera_multi_view_2(self, pi_ip, ports):
        server_addresses = [f"{pi_ip}:{port}" for port in ports]

        self.cameras = CAMERAS(
            labels = [self.cam_4_label, self.cam_5_label, self.cam_6_label],
            combos = [self.cam_1_combo, self.cam_2_combo, self.cam_3_combo],
            toggle_buttons = [self.cam_1_toggle_btn, self.cam_2_toggle_btn, self.cam_3_toggle_btn],
            server_addresses = server_addresses
        )

    def init_camera_primary_view(self, pi_ip, ports):
        server_addresses = [f"{pi_ip}:{port}" for port in ports]

        self.cameras = CAMERAS(
            labels = [self.cam_7_label],
            combos = [self.cam_1_combo],
            toggle_buttons = [self.cam_1_toggle_btn],
            server_addresses = server_addresses
        )
    '''

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

    '''
    def toggle_view_mode(self, pi_ip, ports, ports_2):
        if hasattr(self, "cameras"):
            self.view_switching = True
            self.cameras.set_controls_enabled(False)
            self.cameras.release_captures()

        QTimer.singleShot(250, lambda: self._switch_view_mode_2(pi_ip, ports, ports_2))

    def _switch_view_mode(self, pi_ip, ports):
        if self.current_mode == "multi":
            self.cameras_stacked_widget.setCurrentIndex(1)
            self.init_camera_multi_view_2(pi_ip, ports)
            self.toggle_view_button.setText("Switch to Primary View")
            self.current_mode = "multi-2"

        elif self.current_mode == "multi-2":
            self.cameras_stacked_widget.setCurrentIndex(2)
            self.init_camera_primary_view(pi_ip, ports)
            self.toggle_view_button.setText("Switch to Multi View")
            self.current_mode = "primary"

        else:
            self.cameras_stacked_widget.setCurrentIndex(0)
            self.init_camera_multi_view_1(pi_ip, ports)
            self.toggle_view_button.setText("Switch to Multi-2 View")
            self.current_mode = "multi"

        self.view_switching = False
        if hasattr(self, "cameras"):
            self.cameras.set_controls_enabled(True)

    def _switch_view_mode_2(self, pi_ip, ports, ports_2):
    # Safely stop current camera session
        if hasattr(self, "cameras"):
            self.cameras.release_captures()

        if self.current_mode == "multi":
            self.cameras_stacked_widget.setCurrentIndex(1)
            self.init_camera_multi_view_2(pi_ip, ports)
            self.toggle_view_button.setText("Switch to Multi View")
            self.current_mode = "multi-2"

        else:  # Default to multi
            self.cameras_stacked_widget.setCurrentIndex(0)
            self.init_camera_multi_view_1(pi_ip, ports_2)
            self.toggle_view_button.setText("Switch to Multi-2 View")
            self.current_mode = "multi"

        self.view_switching = False

        # Re-enable controls after switching view
        if hasattr(self, "cameras"):
            self.cameras.set_controls_enabled(True)

    '''

    # ──────────────────────── SHIPWRECK PANEL PAGE SETUP ────────────────────────
    # Sets up all widgets, signals, and logic related to the Shipwreck Panel page.

    def shipwreckPanelTab(self):
        self.shipwreckLogic = SHIPWRECK_LOGIC()

        # Attach image file button
        self.attachFileShipwreckButton = self.ui.findChild(QPushButton, "attachFileShipwreck") 
        self.attachFileShipwreckButton.clicked.connect(lambda: self.shipwreckLogic.shipwreck_length(self))

        # Finish button to identify ship
        self.shipFinishButton = self.ui.findChild(QPushButton, "shipFinishButton")
        self.shipFinishButton.clicked.connect(lambda: self.shipwreckLogic.shipwreck_identifier(self))

        # Labels for displaying ship name and image
        self.shipNameLabel = self.ui.findChild(QLabel, "shipNameDisplay")
        self.shipwreckImageLabel = self.ui.findChild(QLabel, "shipwreckImageLabel")

        # Dropdown menus for ship attributes
        self.shipType_menu = self.ui.findChild(QComboBox, "shipType_menu")
        self.shipLength_menu = self.ui.findChild(QComboBox, "shipLength_menu")
        self.shipCargo_menu = self.ui.findChild(QComboBox, "shipCargo_menu")

        # Finish button to identify ship
        self.shipwreckResetButton = self.ui.findChild(QPushButton, "shipwreckResetButton")
        self.shipwreckResetButton.clicked.connect(self.clear_shipwreck_panel)

        # Clear all menus and add default placeholder
        self.shipType_menu.clear()
        self.shipLength_menu.clear()
        self.shipCargo_menu.clear()

        self.shipType_menu.addItem("Select ship type...")
        self.shipLength_menu.addItem("Select length...")
        self.shipCargo_menu.addItem("Select cargo...")

        # Populate static options
        self.shipType_menu.addItems([
            "freighter - propeller",
            "paddlewheel - octogonal paddlewheel",
            "schooner - brown mast"
        ])

        self.shipLength_menu.addItems([
            "1.27", "1.48", "1.73", "1.97"
        ])

        self.shipCargo_menu.addItems([
            "coal - black",
            "wheat - yellow",
            "bricks - red",
            "furnace sand - white"
        ])

    def clear_shipwreck_panel(self):
        self.shipType_menu.setCurrentIndex(0)
        self.shipLength_menu.setCurrentIndex(0)
        self.shipCargo_menu.setCurrentIndex(0)
        self.shipNameLabel.clear()
        self.shipwreckImageLabel.clear()

    # ──────────────────────── E-DNA PANEL PAGE SETUP ────────────────────────
    # Sets up all widgets, signals, and logic related to the E-DNA Panel page.

    def eDNAPanelTab(self):
        # Find all QLabel widgets
        self.sample1Label = self.ui.findChild(QLabel, "sample1Label")
        self.sample2Label = self.ui.findChild(QLabel, "sample2Label")
        self.sample3Label = self.ui.findChild(QLabel, "sample3Label")
        self.sample4Label = self.ui.findChild(QLabel, "sample4Label")
        self.sample5Label = self.ui.findChild(QLabel, "sample5Label")
        self.sample6Label = self.ui.findChild(QLabel, "sample6Label")
        self.sample7Label = self.ui.findChild(QLabel, "sample7Label")
        self.sample8Label = self.ui.findChild(QLabel, "sample8Label")
        self.sample9Label = self.ui.findChild(QLabel, "sample9Label")
        self.sample10Label = self.ui.findChild(QLabel, "sample10Label")

        # Create a list of labels to pass to the logic class
        self.eDNA_labels = [
            self.sample1Label, self.sample2Label, self.sample3Label, self.sample4Label, self.sample5Label,
            self.sample6Label, self.sample7Label, self.sample8Label, self.sample9Label, self.sample10Label
        ]

        # Instantiate the logic handler with reference to this GUI (self)
        self.eDNA_logic = EDNA_LOGIC(self, self.eDNA_labels)

        # Hook up your buttons to the methods in eDNA_logic
        # Attach File Button
        self.attachFileEDNAButton = self.ui.findChild(QPushButton, "attachFileEDNA")
        self.attachFileEDNAButton.clicked.connect(self.eDNA_logic.identify_invasive_carp)

        # Manual Input Button
        self.eDNAFailsafeButton = self.ui.findChild(QPushButton, "eDNAFailsafeButton")
        self.eDNAFailsafeButton.clicked.connect(self.eDNA_logic.identify_invasive_carp_failsafe)

        # Clear Results Button
        self.eDNAClearResultsButton = self.ui.findChild(QPushButton, "eDNAClearResultsButton")
        self.eDNAClearResultsButton.clicked.connect(self.eDNA_logic.clear_results)
    

    # ──────────────────────── MAPPING PANEL PAGE SETUP ────────────────────────
    # Sets up all widgets, signals, and logic related to the Mapping Panel page.

    def mappingPanelTab(self):

        # Find's image path and converts image into a Pixmap
        self.mapLabel = self.ui.findChild(QLabel, "mapLabel")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        map_path = os.path.join(base_dir, 'libraries', 'mapping', 'region_images', 'Location-of-the-Illinois-River-basin.png')
        map_pixmap = QPixmap(map_path)

        # Call class library from mapping
        self.model = CARP_REGION_MODEL(self.mapLabel, self)

        # Scale to 60% to Pixmap of original size
        scaled_pixmap = self.model.scale_pixmap(map_pixmap, 0.45)
        self.mapLabel.setPixmap(scaled_pixmap)

        # Mapping Panel UI Controls
        self.attachFileMapButton = self.ui.findChild(QPushButton, "attachFileMapping")
        self.attachFileMapButton.clicked.connect(self.model.model_map_regions)

        self.previousButton = self.ui.findChild(QPushButton, "previous")
        self.previousButton.clicked.connect(self.model.previous_map)

        self.nextButton = self.ui.findChild(QPushButton, "next")
        self.nextButton.clicked.connect(self.model.next_map)

        self.mappingFailsafeButton = self.ui.findChild(QPushButton, "mappingFailsafeButton")
        self.mappingFailsafeButton.clicked.connect(self.model.model_map_regions_failsafe)

        self.mappingResetButton = self.ui.findChild(QPushButton, "mappingResetButton")
        self.mappingResetButton.clicked.connect(self.clearMap)

    def clearMap(self):
        self.mapLabel = self.ui.findChild(QLabel, "mapLabel")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        map_path = os.path.join(base_dir, 'libraries', 'mapping', 'region_images', 'Location-of-the-Illinois-River-basin.png')
        map_pixmap = QPixmap(map_path)

        self.mapLabel.clear()
        scaled_pixmap = self.model.scale_pixmap(map_pixmap, 0.45)
        self.mapLabel.setPixmap(scaled_pixmap)

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
    import os
    os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false"

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