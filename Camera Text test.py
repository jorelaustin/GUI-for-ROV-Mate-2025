import sys
import cv2
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, QGraphicsOpacityEffect
)

class WebcamHUD(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webcam HUD")
        self.setGeometry(100, 100, 800, 600)

        # Webcam display
        self.video_label = QLabel(self)
        self.video_label.setGeometry(0, 0, 800, 600)
        self.video_label.setScaledContents(True)

        # Text overlay
        self.text = "welcome to Crush Depth"
        self.text_overlay = QLabel(self.text, self)
        self.text_overlay.setStyleSheet("color: blue; font-size: 32px; font-weight: bold;")
        self.text_overlay.move(20, 20)  # Text positioning to the top left
        self.text_overlay.resize(400, 50)  # Set fixed size
        self.text_overlay.setAttribute(Qt.WA_TransparentForMouseEvents)


        self.cap = cv2.VideoCapture(0) # OpenCV camera
        if not self.cap.isOpened(): # Conditional function if the camera is not working
            self.text_overlay.setText("No camera found.") 
        else:
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)

    def change_text(self, text):
        self.text = text
        

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.video_label.setPixmap(pixmap)

            self.text_overlay.setText(self.text)

    def resizeEvent(self, event):  # Resize video and overlay to fill window
        self.video_label.resize(self.size())
        self.text_overlay.move(20, 20)
        return super().resizeEvent(event)

    def closeEvent(self, event):
        if self.cap.isOpened():
            self.cap.release()
        event.accept()

    def keyPressEvent(self, event): # This function closes the application if q is entered
        if event.key() == Qt.Key_Q:  
            self.close()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebcamHUD()
    window.show()
    NewText = input('Please input your velocity: ')
    window.change_text(NewText)

    sys.exit(app.exec())
