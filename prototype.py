import sys
import pandas as pd
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtUiTools import QUiLoader

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file dynamically
        loader = QUiLoader()
        self.ui = loader.load("main.ui", self)  # Ensure "main.ui" is in the same directory

        # Connect the QAction "actionQuit" to quit the application
        if hasattr(self.ui, 'actionQuit'):  # Ensure 'actionQuit' exists in the UI
            self.ui.actionQuit.triggered.connect(QApplication.instance().quit)  # Quit the application


        if hasattr(self.ui, 'attachFile'):
            self.ui.attachFile.clicked.connect(self.open_file_dialog)

        

# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())