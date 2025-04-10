import sys
import pandas as pd
import json
from PySide6.QtGui import QAction
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QCoreApplication, QTimer, QFile
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QPushButton, QTabWidget, 
QTableWidgetItem, QTableWidget, QDialog, QVBoxLayout)

class OpenFileDialogWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        file = QFile("ui/file_dialog.ui")  # Path to your UI file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file) # Organize the UIs into folder and find them.

        # Set the layout of this QDialog to hold the loaded UI
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Set window title and fit the contents
        self.adjustSize()
        self.setWindowTitle("JSON to CSV Viewer")

        # Delay file dialog until UI is fully shown
        QTimer.singleShot(0, self.open_file_dialog)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select a JSON File", "", "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            self.convert_json_to_table(file_path)
        else:
            self.reject()  # Close the dialog if no file is selected

    def convert_json_to_table(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)
            df = pd.DataFrame(json_data)
            self.display_csv_in_table(df)
        except Exception as e:
            print(f"Error loading JSON: {e}")
            self.reject()

    def display_csv_in_table(self, df):
        table = self.ui.tableWidget
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[row, col]))
                table.setItem(row, col, item)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file dynamically
        loader = QUiLoader()
        file = QFile("ui/main.ui")  # Path to your UI file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)  # Loads in "main.ui" 
        self.setCentralWidget(self.ui)
        self.setWindowTitle("ROV Dashboard")  

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
            # raise ValueError("Quit action 'actionQuit' not found in UI file.")

        # Connect the QPushButton "attachFile" to quit the application
        if self.button_attachFile:
            print("attachFile exists")
            self.button_attachFile.clicked.connect(self.open_file_dialog)
        else: 
            print("attachFile button does not exist")
            # raise ValueError("Attach file button 'attachFile' not found in UI file.")

    def open_file_dialog(self):
        self.dialog = OpenFileDialogWindow(self)
        self.dialog.show()

# Set the attribute BEFORE creating QApplication
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.show() # Remove this if on
sys.exit(app.exec())