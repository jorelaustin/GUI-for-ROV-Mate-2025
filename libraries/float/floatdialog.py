# This Python file uses the following encoding: utf-8
import sys
import serial
import re
import json
import threading
from PySide6.QtWidgets import QApplication, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic floatDialog.ui -o floatDialog_ui.py
from libraries.float.floatDialog_ui import Ui_FloatDialog

class FLOAT_DIALOG(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FloatDialog()
        self.ui.setupUi(self)

        self.messageInput = self.ui.messageInput
        self.floatSendButton = self.ui.floatSend
        self.floatGoButton = self.ui.floatGo
        self.floatStopButton = self.ui.floatStop
        self.messageSent = self.ui.messageSent
        self.messageReceived = self.ui.messageReceived

        self.floatSendButton.clicked.connect(self.send_message)
        self.floatGoButton.clicked.connect(self.go)
        self.floatStopButton.clicked.connect(self.stop)

        #self.PORT = '/dev/cu.usbserial-0001'
        self.BAUD = 115200
        #self.SER = serial.Serial(self.PORT, self.BAUD)

    def go(self):
        self.receiving = True
        threading.Thread(target=self.receive_message, daemon=False).start()

        message = "AT+SEND=116,1,1"
        self.SER.write(message.encode('utf-8'))
        self.SER.write(bytes('\n', encoding='utf-8'))
        self.messageSent.setText(f"MESSAGE SENT: {message}")

    def receive_message(self):
        outputFilePath = "./temp.json"
        outputFile = open(outputFilePath, "w")
        outputFile.write("[\n")  # Start JSON array

        # This list will hold each cleaned JSON object
        json_objects = []

        while self.receiving:
            message = self.SER.readline().decode('utf-8', errors='ignore').strip()
            self.messageReceived.setText(f"MESSAGE RECEIVED: {message}")

            match = re.search(r'\{(.*?)\}', message)
            if match:
                json_str = "{" + match.group(1) + "}"
                try:
                    data = json.loads(json_str)
                    mapped = {
                        "Company": data.get("c"),
                        "Time (s)": data.get("t"),
                        "Pressure (mBar)": data.get("p"),
                        "Depth (m)": data.get("d")
                    }
                    json_line = json.dumps(mapped) + ",\n"
                    outputFile.write(json_line)
                    print("Written:", json_line.strip())
                except json.JSONDecodeError:
                    print("Invalid JSON:", json_str)

        outputFile.seek(outputFile.tell() - 2, 0)  # Remove last comma
        outputFile.write("\n]\n")  # Close JSON array
        outputFile.close()

    def stop(self):
        self.receiving = False

        message = "AT+SEND=116,1,0"
        self.SER.write(message.encode('utf-8'))
        self.SER.write(bytes('\n', encoding='utf-8'))
        self.messageSent.setText(f"MESSAGE SENT: {message}")

    def send_message(self):
        message = self.messageInput.toPlainText()
        self.SER.write(message.encode('utf-8'))
        self.SER.write(bytes('\n', encoding='utf-8'))
        self.messageSent.setText(f"MESSAGE SENT: {message}")
