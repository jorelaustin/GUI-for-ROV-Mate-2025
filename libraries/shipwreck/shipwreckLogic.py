import math
import cv2
import pyautogui
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt


class SHIPWRECK_LOGIC:
    def shipwreck_length(self, parent):
        parent.state = 0

        file_path, _ = QFileDialog.getOpenFileName(
            parent, "Select a .jpg File", "", "jpg Files (*.jpg);;All Files (*)"
        )

        def distance(p1, p2):
            return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                points.append((x, y))
                cv2.circle(img, (x, y), 9, (255, 255, 255), 2)
                cv2.circle(img, (x, y), 7, (0, 0, 0), -1)
                if len(points) == 2 and parent.state == 0:
                    dist = distance(points[-1], points[-2])
                    cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)
                    parent.scale = dist / (33.0 / 100)
                    parent.state = 1
                    points.clear()
                elif len(points) == 2 and parent.state == 1:
                    dist = distance(points[-1], points[-2])
                    cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)
                    size = dist / parent.scale
                    size += 0.2794 + 0.3
                    cv2.putText(img, f"Size: {size:.2f}", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 0), 10)
                    cv2.putText(img, f"Size: {size:.2f}", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 2)
                    parent.state = 2

        img = cv2.imread(file_path)
        if img is None:
            return

        screen_width, screen_height = pyautogui.size()
        img_height, img_width = img.shape[:2]
        scale_w = (screen_width * 0.7) / img_width
        scale_h = (screen_height * 0.7) / img_height
        scale = min(scale_w, scale_h)
        img = cv2.resize(img, (int(img_width * scale), int(img_height * scale)))
        points = []

        while True:
            cv2.imshow("image", img)
            cv2.setMouseCallback("image", click_event)
            cv2.waitKey(25)
            if parent.state == 2:
                cv2.destroyAllWindows()
                break

        height, width = img.shape[:2]
        width = int(width / 1.5)
        height = int(height / 1.5)

        pixmap = self.convertCvImage2QtImage(img)
        scaled = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        parent.shipwreckImageLabel.setPixmap(scaled)

    def convertCvImage2QtImage(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb_image.shape
        bytes_per_line = channels * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_image)

    def shipwreck_identifier(self, parent):
        shipType = str(parent.shipType_menu.currentText())
        shipLength = str(parent.shipLength_menu.currentText())
        shipCargo = str(parent.shipCargo_menu.currentText())

        ship_database = {
            'freighter - propeller': {
                ('coal - black', '1.73'): "NORMAN",
                ('wheat - yellow', '1.48'): "OHIO",
                ('wheat - yellow', '1.97'): "FLORIDA"
            },
            'paddlewheel - octogonal paddlewheel': {
                ('bricks - red', '1.48'): "MARINE CITY",
                ('coal - black', '1.97'): "ALBANY",
                ('furnace sand - white', '1.27'): "NEW ORLEANS"
            },
            'schooner - brown mast': {
                ('bricks - red', '1.73'): "IRONTON",
                ('furnace sand - white', '1.48'): "M.F. MERRICK",
                ('wheat - yellow', '1.27'): "CORNELIA B. WINDIATE"
            }
        }

        ship_name = ship_database.get(shipType, {}).get((shipCargo, shipLength), "SHIP NOT FOUND")
        parent.shipNameLabel.setText(f"{ship_name}")
