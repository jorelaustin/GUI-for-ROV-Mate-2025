import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton, QFrame
)

class EntryWidget(QWidget):
    def __init__(self, row_data, column_names):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Only show the 'timestamp' column
        if "timestamp" in column_names:
            index = column_names.index("timestamp")
            timestamp_label = QLabel(str(row_data[index]))
            timestamp_label.setStyleSheet("color: black; font-size: 16px;")
            layout.addWidget(timestamp_label)

            # Spacer to push button to the right
            layout.addStretch()

            # Button on the right
            button = QPushButton("View")
            button.setStyleSheet("padding: 4px 12px;")
            button.clicked.connect(lambda: print(f"Button clicked!"))

            layout.addWidget(button)

        self.setStyleSheet("""
            QWidget {
                padding: 10px;
                color: black;
            }
        """)

class DatabaseViewer(QWidget):
    def __init__(self, db_path):
        super().__init__()
        self.setWindowTitle("Custom DB Viewer")
        self.resize(600, 600)

        main_layout = QVBoxLayout(self)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        container = QWidget()
        self.entries_layout = QVBoxLayout(container)
        self.entries_layout.setSpacing(10)

        scroll_area.setWidget(container)

        self.load_data(db_path)

    def load_data(self, db_path):
        connection = sqlite3.connect("database/drone_data.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM metadata")  # Replace with your table name
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        for i, row_data in enumerate(rows):
            entry_widget = EntryWidget(row_data, column_names)
            self.entries_layout.addWidget(entry_widget)

             # Add a separator line after each EntryWidget (except the last one)
            if i < len(rows) - 1:
                line = QFrame()
                line.setFrameShape(QFrame.HLine)
                line.setFrameShadow(QFrame.Sunken)
                line.setStyleSheet("color: gray; ")
                self.entries_layout.addWidget(line)

        connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DatabaseViewer("your_database.db")  # Replace with your actual .db path
    viewer.show()
    sys.exit(app.exec())
