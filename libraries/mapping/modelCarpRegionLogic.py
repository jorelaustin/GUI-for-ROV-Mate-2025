import cv2
import pandas as pd
import os
from PySide6.QtCore import Qt, QObject, Signal, QFile
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QFileDialog, QApplication, QDialog, QComboBox, QPushButton
from PySide6.QtUiTools import QUiLoader

class MappingFailsafe(QDialog):
    mapsReady = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()

        ui_path = os.path.join(os.path.dirname(__file__), "..", "..", "ui", "mapping_failsafe_dialog.ui")
        ui_path = os.path.normpath(ui_path)  # normalize slashes for Windows
        file = QFile(ui_path)  # Path to your UI file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file) # Organize the UIs into folder and find them.

        # Set window title and fit the contents
        self.adjustSize()
        self.setWindowTitle("Mapping Fail-Safe Program")

        self.menu2016 = self.ui.findChild(QComboBox, "comboBox_2016")
        self.menu2017 = self.ui.findChild(QComboBox, "comboBox_2017")
        self.menu2018 = self.ui.findChild(QComboBox, "comboBox_2018")
        self.menu2019 = self.ui.findChild(QComboBox, "comboBox_2019")
        self.menu2020 = self.ui.findChild(QComboBox, "comboBox_2020")
        self.menu2021 = self.ui.findChild(QComboBox, "comboBox_2021")
        self.menu2022 = self.ui.findChild(QComboBox, "comboBox_2022")
        self.menu2023 = self.ui.findChild(QComboBox, "comboBox_2023")
        self.menu2024 = self.ui.findChild(QComboBox, "comboBox_2024")
        self.menu2025 = self.ui.findChild(QComboBox, "comboBox_2025")

        # List of region choices
        region_options = ["Select Region..."] + [f"Region {i}" for i in range(1, 6)]

        # Populate all combo boxes with the same region options
        for menu in [
            self.menu2016, self.menu2017, self.menu2018, self.menu2019, self.menu2020,
            self.menu2021, self.menu2022, self.menu2023, self.menu2024, self.menu2025
        ]:
            menu.addItems(region_options)

        # Finish fail-safe button
        self.finishButton = self.ui.self.ui.findChild(QPushButton, "failsafeFinishButton")
        self.finishButton.clicked.connect(self.model_carp_region_manual)

class CARP_REGION_MODEL(QObject):
    def __init__(self, map_label, parent=None):
        super().__init__(parent)
        self.mapLabel = map_label
        self.maps = []
        self.mapIndex = 0

    def scale_pixmap(self, pixmap, scale_factor=0.45):
        width = int(pixmap.width() * scale_factor)
        height = int(pixmap.height() * scale_factor)
        return pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def convertCvImage2QtImage(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb_image.shape
        bytes_per_line = channels * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_image)

    def model_map_regions(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select CSV", "", "CSV Files (*.csv)")
        if not file_path:
            return

        CARP_DATA = pd.read_csv(file_path, dtype=str)
        self.maps = []

        for i in range(CARP_DATA.shape[0]):
            year = CARP_DATA.iloc[i, 0]
            truths = CARP_DATA.iloc[i, 1:6].tolist()
            mapBackground = cv2.imread('libraries/mapping/region_images/Location-of-the-Illinois-River-basin.png')
            HEIGHT, WIDTH = mapBackground.shape[:2]

            for j, truth in enumerate(truths):
                if truth == "Y":
                    path = f'libraries/mapping/region_images/Region {j+1} MAP.png'
                    mapBackground = self.add_region(mapBackground, path, WIDTH, HEIGHT)

            mapBackground = cv2.putText(mapBackground, year, (50, 1200), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 0), 2)
            self.maps.append(mapBackground)

        self.mapIndex = 0
        pixmap = self.convertCvImage2QtImage(self.maps[self.mapIndex])
        self.mapLabel.setPixmap(self.scale_pixmap(pixmap, 0.5))

    def model_map_regions_failsafe(self):
        self.mappingDialog = MappingFailsafe()
        self.mappingDialog.mapsReady.connect(self.maps_from_failsafe)
        self.mappingDialog.show()
        self.mapIndex = 0

    def maps_from_failsafe(self, maps):
        self.maps = maps
        self.mapIndex = 0
        pixmap = self.convertCvImage2QtImage(self.maps[self.mapIndex])
        scaled = self.scale_pixmap(pixmap, 0.5)
        self.mapLabel.setPixmap(scaled)

    def previous_map(self):
        if self.mapIndex > 0:
            self.mapIndex -= 1
            pixmap = self.convertCvImage2QtImage(self.maps[self.mapIndex])
            self.mapLabel.setPixmap(self.scale_pixmap(pixmap, 0.5))

    def next_map(self):
        if self.mapIndex < len(self.maps) - 1:
            self.mapIndex += 1
            pixmap = self.convertCvImage2QtImage(self.maps[self.mapIndex])
            self.mapLabel.setPixmap(self.scale_pixmap(pixmap, 0.5))

    def add_region(self, mapBackground, foregroundPath, WIDTH, HEIGHT):
        regionForeground = cv2.imread(foregroundPath)
        if regionForeground is None:
            print(f"⚠️ Couldn't read: {foregroundPath}")
            return mapBackground

        regionForeground = cv2.resize(regionForeground, (WIDTH, HEIGHT))
        regionAlpha = regionForeground[:, :, 2]
        _, regionMask = cv2.threshold(regionAlpha, 10, 255, cv2.THRESH_BINARY)
        regionMaskInv = cv2.bitwise_not(regionMask)
        mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionMaskInv)
        regionMasked = cv2.bitwise_and(regionForeground, regionForeground, mask=regionMask)
        return cv2.add(mapBackground, regionMasked)
    
    def model_carp_region_manual(self):
        
        # Set the location, font, font size, color, and line thickness for the text (year counter)
        ORG = (50, 1200)
        FONT = cv2.FONT_HERSHEY_DUPLEX
        FONT_SCALE = 2
        COLOR = (0, 0, 0)
        THICKNESS = 2

        self.maps = []
        menus = [
            self.menu2016,
            self.menu2017,
            self.menu2018,
            self.menu2019,
            self.menu2020,
            self.menu2021,
            self.menu2022,
            self.menu2023,
            self.menu2024,
            self.menu2025,
        ]

        for i, menu in enumerate(menus):
            map = cv2.imread('./libraries/mapping/region_images/Location-of-the-Illinois-River-basin.png')
            HEIGHT, WIDTH = map.shape[:2]
            year = str(2016 + i)

            region = str(menu.currentText())
            if (region == "Region 1") or (region == "Region 2") or (region == "Region 3") or (region == "Region 4") or (region == "Region 5"):
                map = self.add_region(map,'./libraries/mapping/region_images/Region 1 MAP.png', WIDTH, HEIGHT)

            if (region == "Region 2") or (region == "Region 3") or (region == "Region 4") or (region == "Region 5"):
                map = self.add_region(map,'./libraries/mapping/region_images/Region 2 MAP.png', WIDTH, HEIGHT)

            if (region == "Region 3") or (region == "Region 4") or (region == "Region 5"):
                map = self.add_region(map,'./libraries/mapping/region_images/Region 3 MAP.png', WIDTH, HEIGHT)

            if (region == "Region 4") or (region == "Region 5"):
                map = self.add_region(map,'./libraries/mapping/region_images/Region 4 MAP.png', WIDTH, HEIGHT)

            if (region == "Region 5"):
                map = self.add_region(map,'./libraries/mapping/region_images/Region 5 MAP.png', WIDTH, HEIGHT)

            map = cv2.putText(map, year, ORG, FONT, FONT_SCALE, COLOR, THICKNESS, cv2.LINE_AA)
            self.maps.append(map) 

        
        self.mapsReady.emit(self.maps)  # Send back to main UI
        self.close()
