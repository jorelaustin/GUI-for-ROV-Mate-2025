# pyside6_viewer.py
import sys
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

from flask_camera_server import run_flask  # Import and run Flask from same project

class CameraViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Three Camera Streams")

        layout = QVBoxLayout()
        self.views = []

        for i in range(3):
            view = QWebEngineView()
            view.load(f"http://localhost:5000/cam{i}")
            layout.addWidget(view)
            self.views.append(view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    # Start Flask in a separate thread
    threading.Thread(target=run_flask, daemon=True).start()

    app = QApplication(sys.argv)
    viewer = CameraViewer()
    viewer.resize(800, 600)
    viewer.show()
    sys.exit(app.exec())
