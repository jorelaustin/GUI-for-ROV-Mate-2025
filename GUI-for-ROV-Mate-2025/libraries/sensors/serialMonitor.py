import sys
import serial
import threading

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PySide6.QtCore import Signal, QObject


class SerialReader(QObject):
    data_received = Signal(str)

    def __init__(self, port, baud=9600):
        super().__init__()
        self.port = port
        self.baud = baud
        self._running = False
        self.ser = None

    def start(self):
        self._running = True
        threading.Thread(target=self.read_serial, daemon=True).start()

    def stop(self):
        self._running = False
        if self.ser and self.ser.is_open:
            self.ser.close()

    def read_serial(self):
        try:
            self.ser = serial.Serial(self.port, self.baud)
            while self._running:
                if self.ser.in_waiting:
                    line = self.ser.readline().decode('utf-8').strip()
                    self.data_received.emit(line)
        except serial.SerialException as e:
            self.data_received.emit(e)

class TetherCounter:
    def connect(self, parent):
        self.tetherReader = SerialReader(port='/dev/tty.usbmodem1101')
        self.tetherReader.start()
        self.tetherReader.data_received.connect(lambda reading: self.display_data(parent, reading))

    def display_data(self, parent, reading):
        parent.tetherDisplay.setText(f"Tether Out: {reading}")

class pHSensor:
    def connect(self, parent):
        self.pHReader = SerialReader(port='/dev/tty.usbmodem113301')
        self.pHReader.start()
        self.pHReader.data_received.connect(lambda reading: self.display_data(parent, reading))

    def display_data(self, parent, reading):
        parent.pHDisplay.setText(f"pH: {reading}")    