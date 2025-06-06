import sqlite3
from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QByteArray, Qt


class ENTRY_WIDGET(QWidget):
    def __init__(self, row_data, column_names, db_path):
        super().__init__()
        self.setObjectName("entryWidget")
        self.db_path = db_path
        self.table_name = row_data[column_names.index("table_name")]
        self.image_data = row_data[column_names.index("image")]

        layout = QVBoxLayout(self)
        row_layout = QHBoxLayout()

        # Timestamp label
        timestamp = row_data[column_names.index("timestamp")]
        timestamp_label = QLabel(str(timestamp))
        timestamp_label.setStyleSheet("color: white; font-size: 20px;")
        row_layout.addWidget(timestamp_label)
        row_layout.addStretch()

        # View button
        self.toggle_button = QPushButton("View")
        self.toggle_button.clicked.connect(self.toggle_dropdown)
        row_layout.addWidget(self.toggle_button)

        # Delete button
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.handle_delete)
        row_layout.addWidget(self.delete_button)

        layout.addLayout(row_layout)

        # Expandable area
        self.dropdown_widget = QWidget()
        self.dropdown_layout = QVBoxLayout(self.dropdown_widget)
        self.dropdown_widget.setVisible(False)
        layout.addWidget(self.dropdown_widget)

    def toggle_dropdown(self):
        if self.dropdown_widget.isVisible():
            self.dropdown_widget.setVisible(False)
            self.toggle_button.setText("View")
        else:
            if self.dropdown_layout.count() == 0:
                self.load_table_data()
            self.dropdown_widget.setVisible(True)
            self.toggle_button.setText("Hide")

    def load_table_data(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute(f"SELECT * FROM '{self.table_name}'")
            rows = cursor.fetchall()
            col_names = [desc[0] for desc in cursor.description]

            table = QTableWidget(len(rows), len(col_names))
            table.setHorizontalHeaderLabels(col_names)
            table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            table.setMinimumWidth(300)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(self.image_data))
            image_label = QLabel()
            image_label.setPixmap(pixmap.scaledToWidth(400, Qt.SmoothTransformation))

            h_widget = QWidget()
            h_layout = QHBoxLayout(h_widget)
            h_layout.setContentsMargins(0, 0, 0, 0)
            h_layout.addWidget(table)
            h_layout.addWidget(image_label)

            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(h_widget)

            self.dropdown_layout.addWidget(scroll_area)

        except sqlite3.Error as e:
            self.dropdown_layout.addWidget(QLabel(f"Error loading table {self.table_name}: {e}"))

        finally:
            conn.close()

    def handle_delete(self):
        confirm = QMessageBox.question(
            self, "Confirm Delete",
            f"Delete entry for '{self.table_name}'?\nThis will also drop the data table.",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM metadata WHERE table_name = ?", (self.table_name,))
                cursor.execute(f"DROP TABLE IF EXISTS '{self.table_name}'")
                conn.commit()
                conn.close()
                self.setParent(None)
                self.deleteLater()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Failed to delete: {e}")

    @staticmethod
    def load_entries_into(container_widget, db_path):
        # Check if layout exists, otherwise create one
        layout = container_widget.layout()
        if layout is None:
            layout = QVBoxLayout(container_widget)
            container_widget.setLayout(layout)
        else:
            # Clear the layout
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)

        layout.setSpacing(10)

        # Load from database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM metadata")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        for i, row_data in enumerate(rows):
            entry_widget = ENTRY_WIDGET(row_data, column_names, db_path)
            layout.addWidget(entry_widget)

            if i < len(rows) - 1:
                line = QFrame()
                line.setFrameShape(QFrame.HLine)
                line.setStyleSheet("color: #fafafa;")
                layout.addWidget(line)

        conn.close()
