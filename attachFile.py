import sys
import pandas as pd
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON to CSV Viewer")

        # Button to attach file
        self.attach_button = QPushButton("Attach JSON File")
        self.attach_button.clicked.connect(self.open_file_dialog)

        # Table widget to display data
        self.table_widget = QTableWidget()

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.attach_button)
        layout.addWidget(self.table_widget)

        # Container widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select a JSON File", "", "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            self.convert_json_to_csv(file_path)

    def convert_json_to_csv(self, file_path):
        try:
            # Read JSON file
            with open(file_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)

            # Convert JSON to DataFrame
            df = pd.DataFrame(json_data)

            # Display CSV Data in Table
            self.display_csv_in_table(df)

        except Exception as e:
            print(f"Error: {e}")

    def display_csv_in_table(self, df):
        self.table_widget.setRowCount(df.shape[0])
        self.table_widget.setColumnCount(df.shape[1])
        self.table_widget.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[row, col]))
                self.table_widget.setItem(row, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
