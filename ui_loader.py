import sys
from PySide6.QtGui import QAction
from PySide6.QtCore import QCoreApplication, QFile, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTabWidget
)
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

# Set the attribute BEFORE creating QApplication
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.showFullScreen() # Remove this if on
sys.exit(app.exec())