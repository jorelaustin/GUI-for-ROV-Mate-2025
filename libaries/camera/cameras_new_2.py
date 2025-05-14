import sys
import os
import cv2
from PySide6.QtCore import QTimer, Qt, QThread, Signal, QObject
from PySide6.QtGui import QImage, QPixmap, QIcon
import time  # For timing analysis


class FrameProcessor(QThread):
    """
    A separate thread to handle frame processing (reading, converting, scaling).
    This prevents blocking the main GUI thread.
    """
    frame_signal = Signal(int, QPixmap)  # Signal to send processed frame and index
    finished_signal = Signal(int)

    def __init__(self, camera_index, capture, label_size, no_signal_path, parent=None):
        super().__init__(parent)
        self.camera_index = camera_index
        self.capture = capture
        self.label_size = label_size
        self.no_signal_path = no_signal_path
        self.running = True  # Control the thread's loop
        self.frame_count = 0
        self.start_time = time.time()

    def run(self):
        """
        Main loop for the thread.  Reads frames, processes them, and emits a signal.
        """
        if self.capture is None:
            no_signal_pixmap = QPixmap(self.no_signal_path)
            scaled_pixmap = no_signal_pixmap.scaled(
                self.label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.frame_signal.emit(self.camera_index, scaled_pixmap)
            self.finished_signal.emit(self.camera_index)  # Emit finished signal
            return

        while self.running:
            ret, frame = self.capture.read()
            if ret and frame is not None:
                self.frame_count += 1

                # Timing (optional, for debugging)
                start_time = time.time()

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                qimg = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg).scaled(
                    self.label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                end_time = time.time()
                # print(f"Processing time for camera {self.camera_index}: {end_time - start_time:.4f} seconds") #remove comment

                self.frame_signal.emit(
                    self.camera_index, pixmap
                )  # Send processed frame and camera index
            else:
                # Handle the case where a frame is not read correctly.
                no_signal_pixmap = QPixmap(self.no_signal_path)
                scaled_pixmap = no_signal_pixmap.scaled(
                    self.label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.frame_signal.emit(self.camera_index, scaled_pixmap)
                self.finished_signal.emit(
                    self.camera_index
                )  # Emit finished signal.  Important for no signal too.
                # Consider adding a small sleep here to prevent a tight loop if the camera disconnects.
                time.sleep(0.01)

    def stop(self):
        """
        Stop the thread's loop.
        """
        self.running = False
        self.quit()  # Cleanly stop the thread.
        self.wait()
        self.finished_signal.emit(
            self.camera_index
        )  # Ensure finished signal is sent on stop


class CAMERAS(QObject):  # Inherit from QObject to use signals
    def __init__(self, labels, combos, toggle_buttons, urls, num_cameras=3, parent=None):
        super().__init__(parent)  # Initialize QObject
        self.num_cameras = num_cameras
        self.labels = labels
        self.combos = combos
        self.toggle_buttons = toggle_buttons
        self.urls = urls  # Store URLs for later use
        self.selected_camera_indices = [0, 1, 2]
        self.feed_enabled = [False] * 3
        self.threads = []  # List to store FrameProcessor threads
        self.captures = []
        self.thread_started = [
            False
        ] * 3  # Track if a thread has been started for each camera

        # Load icon and no signal image path
        icon_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "graphics", "white_camera.png"
        )
        self.icon = QIcon(os.path.normpath(icon_path))
        self.no_signal_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "graphics", "no_signal.png"
        ).replace("\\", "/")

        # Setup widgets
        for i in range(3):
            self.labels[i].setAlignment(Qt.AlignCenter)
            self.labels[i].clear()
            self.combos[i].addItems([f"Camera {j + 1}" for j in range(self.num_cameras)])
            self.combos[i].setCurrentIndex(i)
            self.combos[i].currentIndexChanged.connect(self.update_camera_selection)
            self.toggle_buttons[i].setCheckable(True)
            self.toggle_buttons[i].setChecked(False)
            self.toggle_buttons[i].setIcon(self.icon)
            self.toggle_buttons[i].setStyleSheet("background-color: #424242;")
            self.toggle_buttons[i].toggled.connect(
                lambda checked, idx=i: self.toggle_feed(idx, checked)
            )

        # No timer needed anymore.

    def start_camera_threads(self):
        """
        Start the frame processing threads for each camera.  Call this when the
        application and GUI are ready.
        """
        # Use stored URLs
        for i, url in enumerate(self.urls):
            if url:
                cap = cv2.VideoCapture(url)
                if cap.isOpened():
                    print(f"[Info] Connected to camera stream: {url}")
                    self.captures.append(cap)
                    thread = FrameProcessor(
                        i, cap, self.labels[i].size(), self.no_signal_path
                    )  # Pass the no_signal path
                    thread.frame_signal.connect(
                        self.update_label
                    )  # Connect the signal
                    thread.finished_signal.connect(
                        self.thread_finished
                    )  # Connect finished
                    self.threads.append(thread)
                    self.threads[i].start()
                    self.thread_started[i] = True
                else:
                    print(f"[Warning] Could not open stream: {url}")
                    self.captures.append(None)
                    # Create a "dummy" thread to display "No Signal" even if the camera fails.
                    thread = FrameProcessor(
                        i, None, self.labels[i].size(), self.no_signal_path
                    )
                    thread.frame_signal.connect(self.update_label)
                    thread.finished_signal.connect(
                        self.thread_finished
                    )  # Connect finished
                    self.threads.append(thread)
                    self.threads[i].start()
                    self.thread_started[i] = True
            else:
                print(f"[Warning] No URL provided for camera {i}")
                self.captures.append(None)
                thread = FrameProcessor(
                    i, None, self.labels[i].size(), self.no_signal_path
                )
                thread.frame_signal.connect(self.update_label)
                thread.finished_signal.connect(
                    self.thread_finished
                )  # Connect finished
                self.threads.append(thread)
                self.threads[i].start()
                self.thread_started[i] = True

    def update_camera_selection(self):
        """
        Handles combo box changes to update the selected camera index.
        """
        selected_camera_indices = [combo.currentIndex() for combo in self.combos]
        if self.selected_camera_indices != selected_camera_indices:
            self.selected_camera_indices = selected_camera_indices
            self.update_threads()  # restart threads

    def update_threads(self):
        """
        Restart the threads based on the new camera selection.
        """
        # Stop all existing threads
        for thread in self.threads:
            if thread.isRunning():
                thread.stop()
        for i in range(len(self.threads)):
            self.thread_started[i] = False
        self.threads = []  # clear
        self.captures = []

        # Start threads with the new camera selection
        for i, url in enumerate(self.urls):
            if url:
                cap = cv2.VideoCapture(url)
                if cap.isOpened():
                    print(f"[Info] Connected to camera stream: {url}")
                    self.captures.append(cap)
                    thread = FrameProcessor(
                        i, cap, self.labels[i].size(), self.no_signal_path
                    )
                    thread.frame_signal.connect(self.update_label)
                    thread.finished_signal.connect(
                        self.thread_finished
                    )  # Connect finished
                    self.threads.append(thread)
                    self.threads[i].start()
                    self.thread_started[i] = True
                else:
                    print(f"[Warning] Could not open stream: {url}")
                    self.captures.append(None)
                    thread = FrameProcessor(
                        i, None, self.labels[i].size(), self.no_signal_path
                    )
                    thread.frame_signal.connect(self.update_label)
                    thread.finished_signal.connect(
                        self.thread_finished
                    )  # Connect finished
                    self.threads.append(thread)
                    self.threads[i].start()
                    self.thread_started[i] = True
            else:
                print(f"[Warning] No URL provided for camera {i}")
                self.captures.append(None)
                thread = FrameProcessor(
                    i, None, self.labels[i].size(), self.no_signal_path
                )
                thread.frame_signal.connect(self.update_label)
                thread.finished_signal.connect(
                    self.thread_finished
                )  # Connect finished
                self.threads.append(thread)
                self.threads[i].start()
                self.thread_started[i] = True

    def toggle_feed(self, index, checked):
        """
        Handles toggling the camera feed on or off.
        """
        self.feed_enabled[index] = checked
        if checked:
            self.toggle_buttons[index].setStyleSheet("background-color: #007ACC;")
            if not self.thread_started[
                index
            ]:  # Check if the thread has ever been started
                self.update_threads()
        else:
            self.toggle_buttons[index].setStyleSheet("background-color: #424242;")
            # Stop the corresponding thread
            self.threads[index].stop()
            self.thread_started[index] = (
                False  # Reset the flag when the thread is stopped
            )
            # Show "No Signal" image when toggled off
            no_signal_pixmap = QPixmap(self.no_signal_path)
            scaled_pixmap = no_signal_pixmap.scaled(
                self.labels[index].size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.labels[index].setPixmap(scaled_pixmap)

    def update_label(self, camera_index, pixmap):
        """
        Update the QLabel with the received frame (called via signal from FrameProcessor).
        This runs in the main GUI thread.
        """
        if self.feed_enabled[camera_index]:
            self.labels[camera_index].setPixmap(pixmap)

    def thread_finished(self, camera_index):
        """
        Slot to handle the finished signal from FrameProcessor.
        """
        print(f"Thread for camera {camera_index} finished.")
        self.thread_started[
            camera_index
        ] = False  # Reset the flag when the thread finishes

    def switch_primary_camera_to(self, new_index):
        """
        Switch the primary camera feed.
        """
        if 0 <= new_index < self.num_cameras:
            self.combos[0].setCurrentIndex(new_index)  # Switch the primary feed (index 0)
            print(f"[Info] Switched primary feed to camera index {new_index}")
            # Optionally ensure it's turned on
            if not self.feed_enabled[0]:
                self.toggle_buttons[0].click()  # Programmatically toggle it on

    def set_primary_only_view(self, camera_index=0):
        """
        Display only the primary camera.
        """
        for i in range(3):
            if i == 0:
                # self.combos[i].setCurrentIndex(camera_index)
                self.feed_enabled[i] = True
                self.toggle_buttons[i].setChecked(True)
                self.labels[i].show()
            else:
                self.feed_enabled[i] = False
                self.toggle_buttons[i].setChecked(False)
                self.labels[i].hide()  # Hide the QLabel

    def set_three_camera_view(self):
        """
        Display all three camera feeds.
        """
        for i in range(3):
            # self.combos[i].setCurrentIndex(i)
            self.feed_enabled[i] = True
            self.toggle_buttons[i].setChecked(True)
            self.labels[i].show()  # Make sure all labels are visible

    def release_captures(self):
        """
        Release all camera captures and stop threads.
        """
        for cap in self.captures:
            if cap is not None:
                cap.release()
        for thread in self.threads:
            if thread.isRunning():
                thread.stop()  # Stop the thread cleanly
        for i in range(len(self.threads)):
            self.thread_started[i] = False