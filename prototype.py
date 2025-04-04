import sys
import pandas as pd
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QTabWidget
from PySide6.QtGui import QAction
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

        # Find object and it's name
        self.action_quit = self.ui.findChild(QAction, "actionQuit") # Quit action
        self.button_attachFile = self.ui.findChild(QPushButton, "attachFile") # Attach file button
        self.tab_widget = self.ui.findChild(QTabWidget, "tabWidget") # Tab widget

        # Open up on first tab
        if self.tab_widget:
            print("tabWidget exists")
            self.tab_widget.setCurrentIndex(0)

        # Connect the QAction "actionQuit" to quit the application
        if self.action_quit:  # Ensure 'actionQuit' exists in the UI
            print("actionQuit exists")
            self.action_quit.triggered.connect(QApplication.instance().quit)  # Quit the application
        else:
            print("Quit button does not exist") #Add raise error exception here

        # Connect the QPushButton "attachFile" to quit the application
        if self.button_attachFile:
            print("attachFile exists")
            self.button_attachFile.clicked.connect(self.open_directory)
        else: 
            print("attachFile button does not exist")


    def open_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            print(f"Selected directory: {directory}")

# Set the attribute BEFORE creating QApplication
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())