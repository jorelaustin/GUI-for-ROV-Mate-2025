import sys
import cv2
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QComboBox, QGridLayout
)
from PySide6.QtGui import QImage, QPixmap, QIcon

class CameraWidget(QWidget):
    def __init__(self, camera_id=0, parent=None):
        super().__init__(parent)
        self.camera_id = camera_id
        self.cap = None
        self.is_on = False

        self.video_label = QLabel("Camera feed")
        self.video_label.setFixedSize(320, 240)
        self.video_label.setStyleSheet("background-color: black")

        self.toggle_button = QPushButton("Turn On")
        self.icon = QIcon("graphics\white_camera.png")  # Replace with your image path
        self.toggle_button.setIcon(self.icon)
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;         /* Text color */
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #333;
            }
        """)
        self.toggle_button.clicked.connect(self.toggle_camera)

        self.camera_selector = QComboBox()
        self.camera_selector.addItems([str(i) for i in range(4)])
        self.camera_selector.setCurrentIndex(camera_id)
        self.camera_selector.currentIndexChanged.connect(self.change_camera)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.camera_selector)
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def toggle_camera(self):
        if self.is_on:
            self.stop_camera()
        else:
            self.start_camera()

    def start_camera(self):
        index = int(self.camera_selector.currentText())
        self.cap = cv2.VideoCapture(index)
        if self.cap.isOpened():
            self.is_on = True
            self.toggle_button.setText("Turn Off")
            self.timer.start(30)
        else:
            self.cap = None
            self.video_label.setText("Camera not found")

    def stop_camera(self):
        self.is_on = False
        self.toggle_button.setText("Turn On")
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.video_label.clear()
        self.video_label.setText("Camera feed")

    def change_camera(self, index):
        if self.is_on:
            self.stop_camera()
            self.start_camera()

    def update_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_img)
                
                # Scale the pixmap while keeping the aspect ratio
                scaled_pixmap = pixmap.scaled(
                    self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.video_label.setPixmap(scaled_pixmap)
            else:
                self.video_label.setText("No frame")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Camera Viewer")

        layout = QGridLayout()
        for i in range(4):
            cam_widget = CameraWidget(camera_id=i)
            row, col = divmod(i, 2)
            layout.addWidget(cam_widget, row, col)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
