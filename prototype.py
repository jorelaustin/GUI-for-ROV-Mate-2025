import sys
import pandas as pd
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QCoreApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file dynamically
        loader = QUiLoader()
        self.ui = loader.load("main.ui", self)  # Ensure "main.ui" is in the same directory
        self.setCentralWidget(self.ui)
        self.ui.show()

        # Connect the QAction "actionQuit" to quit the application
        if hasattr(self.ui, 'actionQuit'):  # Ensure 'actionQuit' exists in the UI
            self.ui.actionQuit.triggered.connect(QApplication.instance().quit)  # Quit the application
        else:
            print("Quit button, not working")

        
        

# Set the attribute BEFORE creating QApplication
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())