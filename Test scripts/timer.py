from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import QTimer

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")

        # Main layout
        self.layout = QVBoxLayout(self)

        # Time label
        self.label = QLabel("00:00:00")
        self.label.setStyleSheet("font-size: 40px; color: white;")
        self.layout.addWidget(self.label)

        # Button layout
        button_layout = QHBoxLayout()
        self.layout.addLayout(button_layout)

        # Start/Stop toggle button
        self.toggle_button = QPushButton("Start")
        self.toggle_button.setStyleSheet("background-color: green; color: white; font-size: 20px;")
        self.toggle_button.clicked.connect(self.toggle_timer)
        button_layout.addWidget(self.toggle_button)

        # Reset button
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("background-color: gray; color: white; font-size: 20px;")
        self.reset_button.clicked.connect(self.reset_timer)
        button_layout.addWidget(self.reset_button)

        # QTimer setup
        self.timer = QTimer()
        self.timer.setInterval(10)  # 10ms = 1/100th of a second
        self.timer.timeout.connect(self.update_label)

        self.elapsed_ms = 0
        self.running = False

    def toggle_timer(self):
        if self.running:
            self.timer.stop()
            self.toggle_button.setText("Start")
            self.toggle_button.setStyleSheet("background-color: green; color: white; font-size: 20px;")
        else:
            self.timer.start()
            self.toggle_button.setText("Stop")
            self.toggle_button.setStyleSheet("background-color: red; color: white; font-size: 20px;")
        self.running = not self.running

    def reset_timer(self):
        if not self.running:
            self.elapsed_ms = 0
            self.label.setText("00:00:00")

    def update_label(self):
        self.elapsed_ms += 10
        minutes = self.elapsed_ms // 60000
        seconds = (self.elapsed_ms % 60000) // 1000
        hundredths = (self.elapsed_ms % 1000) // 10
        self.label.setText(f"{minutes:02d}:{seconds:02d}:{hundredths:02d}")

if __name__ == "__main__":
    app = QApplication([])
    window = TimerApp()
    window.setStyleSheet("background-color: black;")
    window.show()
    app.exec()
