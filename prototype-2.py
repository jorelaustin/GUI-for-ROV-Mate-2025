import sys
from PySide6.QtGui import QAction, QFont, QFontDatabase, QKeyEvent
from PySide6.QtCore import QCoreApplication, QFile, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTabWidget
)
from PySide6.QtUiTools import QUiLoader

# For STYLE class
from PySide6.QtWidgets import QFrame, QGridLayout, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QPalette

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

        self.style = STYLE()
        self.style.setStylesheet(QApplication.instance())

        # Find object and it's name
        self.action_quit = self.ui.findChild(QPushButton, "program_exit") # Quit action
        # Connect the QAction "actionQuit" to quit the application
        self.action_quit.clicked.connect(QApplication.instance().quit)  # Quit the application

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.showMaximized()  # Press Esc to go to maximized


class STYLE():
    """
    PURPOSE

    Contains a library of stylesheets and functions to modify the style of the program.
    """
    # VARIABLES
    theme = True

    widgetHeight = 0

    def __init__(self):
        """
        PURPOSE

        Class constructor

        INPUT

        NONE

        RETURNS

        NONE
        """
        pass
    

    def setStylesheet(self, appObject):
        appObject.setStyleSheet(""" 
                 
            #controlPanelButton {
                font-size: 12pt;
                color: white;
                background-color: #007ACC;
                border-radius: 14px;
                padding: 6px 12px;
            }
            
            #program_exit {
                font-size: 12pt;
                color: white;
                background-color: red;
                border-radius: 14px;
                padding: 6px 12px;
            }
                                
            #dataButton, #mapButton{
                font-size: 12pt;
                color: white;
                background-color: #424242;
                border-radius: 14px;
                padding: 6px 12px;
            }

            QWidget {
                background-color: #161616;
                color: white;
            }  
                                
            QGroupBox {
                background-color: #212121
            }

            QComboBox {
                background-color: #424242;
                color: white;
            } 
                                
            #control_panel_camera_widget, #control_panel_functions_widget, #buttonsPanel{
                border: 1px solid #fafafa;
                border-radius: 10px;
            }       
        """)

# Set the attribute BEFORE creating QApplication
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
# Run the application
app = QApplication(sys.argv)

# Load the font file
font_id = QFontDatabase.addApplicationFont("fonts/bahnschrift.ttf")

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
window.showFullScreen() # Remove this if on
sys.exit(app.exec())