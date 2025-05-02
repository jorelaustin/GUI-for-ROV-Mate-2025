import sys
import cv2
from PySide6.QtCore import QTimer, Qt, QFile
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader


class CameraHandler:
    def __init__(self, label, combo_box, toggle_button, parent=None):
        self.label = label
        self.combo_box = combo_box
        self.toggle_button = toggle_button
        self.capture = None
        self.timer = QTimer(parent)
        self.timer.timeout.connect(self.update_frame)

        self.toggle_button.clicked.connect(self.toggle_camera)
        self.combo_box.addItems([str(i) for i in range(4)])

    def toggle_camera(self):
        if self.capture is None:
            cam_index = int(self.combo_box.currentText())
            cap = cv2.VideoCapture(cam_index)
            if cap.isOpened():
                self.capture = cap
                self.toggle_button.setText("Turn Off")
                self.timer.start(30)
            else:
                self.label.setText("Camera not found")
        else:
            self.stop_camera()

    def stop_camera(self):
        if self.capture:
            self.timer.stop()
            self.capture.release()
            self.capture = None
            self.label.clear()
            self.label.setText("Camera feed")
            self.toggle_button.setText("Turn On")

    def update_frame(self):
        if self.capture and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_img)
                scaled_pixmap = pixmap.scaled(
                    self.label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.label.setPixmap(scaled_pixmap)

    def cleanup(self):
        self.stop_camera()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        file = QFile("your_ui_file.ui")  # Replace with actual UI path
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        self.setCentralWidget(self.ui)

        # Initialize camera handlers
        self.cameras = [
            CameraHandler(self.ui.label_cam1, self.ui.combo_cam1, self.ui.btn_toggle1, self),
            CameraHandler(self.ui.label_cam2, self.ui.combo_cam2, self.ui.btn_toggle2, self),
            CameraHandler(self.ui.label_cam3, self.ui.combo_cam3, self.ui.btn_toggle3, self),
            CameraHandler(self.ui.label_cam4, self.ui.combo_cam4, self.ui.btn_toggle4, self),
        ]

    def closeEvent(self, event):
        for cam in self.cameras:
            cam.cleanup()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
