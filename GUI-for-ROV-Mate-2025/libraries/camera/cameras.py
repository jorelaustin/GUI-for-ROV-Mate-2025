import sys
import os
import cv2
import socket
import numpy as np
from PySide6.QtCore import QTimer, Qt, QThread, Signal, QObject, Slot
from PySide6.QtGui import QImage, QPixmap, QIcon

class CameraWorker(QObject):
    frame_ready = Signal(int, object)

    def __init__(self, index, ip_address):
        super().__init__()
        parts = ip_address.split(':')
        self.index = index
        self.ip_address = parts[0]
        self.port = int(parts[1])
        print(f"IP Address: {parts[0]}")
        print(f"IP Address: {parts[1]}")
        self.running = False
        self.cap = None
        self.sock = None # Initialize socket attribute

    @Slot()
    def start(self):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Assign to self.sock
        self.sock.bind((self.ip_address, self.port))

        while self.running:
            try:
                packet, _ = self.sock.recvfrom(65536)
                frame = cv2.imdecode(np.frombuffer(packet, dtype=np.uint8), 1)
                if frame is not None: # Check if frame was successfully decoded
                    self.frame_ready.emit(self.index, frame)
            except socket.timeout: # Add timeout handling if you set a timeout
                continue
            except Exception as e:
                print(f"Error receiving frame for camera {self.index}: {e}")
                break # Exit loop on unhandled errors

    def stop(self):
        self.running = False
        if self.sock:
            self.sock.close() # Close the socket
            print(f"Camera {self.index} socket closed.")
        if self.cap:
            self.cap.release()

class CAMERAS:
    def __init__(self, labels, combos, toggle_buttons, server_addresses, num_cameras=3):
        self.num_cameras = num_cameras
        self.labels = labels
        self.combos = combos
        self.toggle_buttons = toggle_buttons

        self.selected_camera_indices = [0, 1, 2]
        self.feed_enabled = [False] * 3
        self.frames = [None] * self.num_cameras

        self.threads = []
        self.workers = []

        # Load icon and no signal image path
        icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "graphics", "white_camera.png")
        self.icon = QIcon(os.path.normpath(icon_path))
        self.no_signal_path = os.path.join(os.path.dirname(__file__), "..", "..", "graphics", "no_signal.png").replace("\\", "/")

        for i in range(self.num_cameras):
            self.labels[i].setAlignment(Qt.AlignCenter)
            self.labels[i].clear()

            self.combos[i].addItems([f"Camera {j+1}" for j in range(self.num_cameras)])
            self.combos[i].setCurrentIndex(i)
            self.combos[i].currentIndexChanged.connect(self.update_camera_selection)

            self.toggle_buttons[i].setCheckable(True)
            self.toggle_buttons[i].setChecked(False)
            self.toggle_buttons[i].setIcon(self.icon)
            self.toggle_buttons[i].setStyleSheet("background-color: #424242;")
            self.toggle_buttons[i].toggled.connect(lambda checked, idx=i: self.toggle_feed(idx, checked))

            # CHANGED
            ip_address = server_addresses[i] if i < len(server_addresses) else None
            if ip_address:
                thread = QThread()
                worker = CameraWorker(i, ip_address)
                worker.moveToThread(thread)
                worker.frame_ready.connect(self.handle_frame)
                thread.started.connect(worker.start)
                thread.start()
                self.threads.append(thread)
                self.workers.append(worker)
            else:
                print(f"[Warning] No IP address for camera {i}")
                self.threads.append(None)
                self.workers.append(None)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frames)
        self.timer.start(30)

    @Slot(int, object)
    def handle_frame(self, index, frame):
        self.frames[index] = frame

    def update_camera_selection(self):
        self.selected_camera_indices = [combo.currentIndex() for combo in self.combos]

    def toggle_feed(self, index, checked):
        self.feed_enabled[index] = checked
        if checked:
            self.toggle_buttons[index].setStyleSheet("background-color: #007ACC;")
        else:
            self.toggle_buttons[index].setStyleSheet("background-color: #424242;")
            no_signal_pixmap = QPixmap(self.no_signal_path)
            scaled_pixmap = no_signal_pixmap.scaled(
                self.labels[index].size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.labels[index].setPixmap(scaled_pixmap)

    def update_frames(self):
        for i in range(3):
            cam_index = self.selected_camera_indices[i]

            if not self.feed_enabled[i]:
                black_pixmap = QPixmap(self.labels[i].size())
                black_pixmap.fill(Qt.black)
                self.labels[i].setPixmap(black_pixmap)
                continue

            if cam_index >= len(self.frames):
                continue

            frame = self.frames[cam_index]

            if frame is None:
                no_signal_pixmap = QPixmap(self.no_signal_path)
                scaled_pixmap = no_signal_pixmap.scaled(
                    self.labels[i].size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.labels[i].setPixmap(scaled_pixmap)
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            bytes_per_line = ch * w
            qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg).scaled(
                self.labels[i].size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.labels[i].setPixmap(pixmap)

    def switch_primary_camera_to(self, new_index):
        if 0 <= new_index < self.num_cameras:
            self.combos[0].setCurrentIndex(new_index)
            print(f"[Info] Switched primary feed to camera index {new_index}")
            if not self.feed_enabled[0]:
                self.toggle_buttons[0].click()

    def set_primary_only_view(self, camera_index=0):
        for i in range(3):
            if i == 0:
                self.feed_enabled[i] = True
                self.toggle_buttons[i].setChecked(True)
                self.labels[i].show()
            else:
                self.feed_enabled[i] = False
                self.toggle_buttons[i].setChecked(False)
                self.labels[i].hide()

    def set_three_camera_view(self):
        for i in range(3):
            self.feed_enabled[i] = True
            self.toggle_buttons[i].setChecked(True)
            self.labels[i].show()

    def release_captures(self):
        for worker in self.workers:
            if worker:
                worker.stop()

        for thread in self.threads:
            if thread:
                thread.quit()
                thread.wait()
