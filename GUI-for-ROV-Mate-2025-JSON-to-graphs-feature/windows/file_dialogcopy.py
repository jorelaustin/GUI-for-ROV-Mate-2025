import os
import pandas as pd
import cv2


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PySide6.QtCore import QTimer, QFile
from PySide6.QtWidgets import (
    QDialog, QFileDialog, QVBoxLayout, QLabel
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class OpenCSVFileDialogWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()

        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "model_carp.ui")
        ui_path = os.path.normpath(ui_path)  # normalize slashes for Windows
        file = QFile(ui_path)  # Path to your UI file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file) # Organize the UIs into folder and find them.

        # Set the layout of this QDialog to hold the loaded UI
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Set window title and fit the contents
        self.adjustSize()
        self.setWindowTitle("Model Carp Regions")

        # Find object and it's name
       # self.x_axis_combo = self.ui.findChild(QComboBox, "xAxisComboBox")
       # self.y_axis_combo = self.ui.findChild(QComboBox, "yAxisComboBox")
       # self.plot_button = self.ui.findChild(QPushButton, "plotButton")
       # self.plot_button.setEnabled(False) # Disable initially
       # self.save_button = self.ui.findChild(QPushButton, "saveFilesButton")

        # Delay file dialog until UI is fully shown
        QTimer.singleShot(0, self.open_CSV_file_dialog)

    def open_CSV_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select a CSV File", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            self.model_carp_regions(file_path)
        else:
            self.reject()  # Close the dialog if no file is selected
    
    def model_carp_regions(self, file_path):
        # Read the data table as a string
        CARP_DATA = pd.read_csv(file_path,dtype=str)

        # Set the location, font, font size, color, and line thickness for the text (year counter)
        ORG = (50, 1200)
        FONT = cv2.FONT_HERSHEY_DUPLEX
        FONT_SCALE = 2
        COLOR = (0, 0, 0)
        THICKNESS = 2
        
        for i in range(CARP_DATA.shape[0]):
            # Index the year and truth value of each region
            year = CARP_DATA.iloc[i,0]
            regionOneTruth = CARP_DATA.iloc[i,1]
            regionTwoTruth = CARP_DATA.iloc[i,2]
            regionThreeTruth = CARP_DATA.iloc[i,3]
            regionFourTruth = CARP_DATA.iloc[i,4]
            regionFiveTruth = CARP_DATA.iloc[i,5]

            # Read the background image, and the height and width of the image
            # Do this every time to reset the map between years
            mapBackground = cv2.imread('regionPNGS/Location-of-the-Illinois-River-basin.png')
            HEIGHT, WIDTH = mapBackground.shape[:2]

            if regionOneTruth == "Y":
                # Read the foreground image and set to the dimensions of the background
                regionOneForeground = cv2.imread('regionPNGS/Region 1 MAP.png')
                regionOneForeground = cv2.resize(regionOneForeground, (WIDTH, HEIGHT))
                # Make the foreground image on a transparent background
                regionOneAlpha = regionOneForeground[:, :, 2] 
                # Turn the foreground image black and white
                regionOneRet, regionOneMask = cv2.threshold(regionOneAlpha, 10, 255, cv2.THRESH_BINARY)
                # Invert the black and white foreground image
                regionOneMaskInv = cv2.bitwise_not(regionOneMask)
                # Black-out the area of the foreground image on the background
                mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionOneMaskInv)
                # Separate the foreground area from the transparent background
                regionOneForegroundMasked = cv2.bitwise_and(regionOneForeground, regionOneForeground, mask=regionOneMask)
                # Add the foreground area ontop of the background
                mapBackground = cv2.add(mapBackground, regionOneForegroundMasked)

            if (regionTwoTruth == "Y"):
                regionTwoForeground = cv2.imread('regionPNGS/Region 2 MAP.png')
                regionTwoForeground = cv2.resize(regionTwoForeground, (WIDTH, HEIGHT))
                regionTwoAlpha = regionTwoForeground[:, :, 2] 
                regionTwoRet, regionTwoMask = cv2.threshold(regionTwoAlpha, 10, 255, cv2.THRESH_BINARY)
                regionTwoMaskInv = cv2.bitwise_not(regionTwoMask)
                mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionTwoMaskInv)
                regionTwoForegroundMasked = cv2.bitwise_and(regionTwoForeground, regionTwoForeground, mask=regionTwoMask)
                mapBackground = cv2.add(mapBackground, regionTwoForegroundMasked)

            if (regionThreeTruth == "Y"):
                regionThreeForeground = cv2.imread('regionPNGS/Region 3 MAP.png')
                regionThreeForeground = cv2.resize(regionThreeForeground, (WIDTH, HEIGHT))
                regionThreeAlpha = regionThreeForeground[:, :, 2] 
                regionThreeRet, regionThreeMask = cv2.threshold(regionThreeAlpha, 10, 255, cv2.THRESH_BINARY) 
                regionThreeMaskInv = cv2.bitwise_not(regionThreeMask)
                mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionThreeMaskInv) 
                regionThreeForegroundMasked = cv2.bitwise_and(regionThreeForeground, regionThreeForeground, mask=regionThreeMask)
                mapBackground = cv2.add(mapBackground, regionThreeForegroundMasked)

            if (regionFourTruth == "Y"):
                regionFourForeground = cv2.imread('regionPNGS/Region 4 MAP.png')
                regionFourForeground = cv2.resize(regionFourForeground, (WIDTH, HEIGHT))
                regionFourAlpha = regionFourForeground[:, :, 2] 
                regionFourRet, regionFourMask = cv2.threshold(regionFourAlpha, 10, 255, cv2.THRESH_BINARY)
                regionFourMaskInv = cv2.bitwise_not(regionFourMask)
                mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionFourMaskInv)
                regionFourForegroundMasked = cv2.bitwise_and(regionFourForeground, regionFourForeground, mask=regionFourMask)
                mapBackground = cv2.add(mapBackground, regionFourForegroundMasked)

            if (regionFiveTruth == "Y"):
                regionFiveForeground = cv2.imread('regionPNGS/Region 5 MAP.png')
                regionFiveForeground = cv2.resize(regionFiveForeground, (WIDTH, HEIGHT))
                regionFiveAlpha = regionFiveForeground[:, :, 2] 
                regionFiveRet, regionFiveMask = cv2.threshold(regionFiveAlpha, 10, 255, cv2.THRESH_BINARY)
                regionFiveMaskInv = cv2.bitwise_not(regionFiveMask) 
                mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionFiveMaskInv)
                regionFiveForegroundMasked = cv2.bitwise_and(regionFiveForeground, regionFiveForeground, mask=regionFiveMask)
                mapBackground = cv2.add(mapBackground, regionFiveForegroundMasked)

            # Add the modeled year to the map
            mapBackground = cv2.putText(mapBackground, year, ORG, FONT, FONT_SCALE, COLOR, THICKNESS, cv2.LINE_AA)

            # Display the modeled year until user quits with key input
            cv2.imshow('Carp Movement', mapBackground)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
                
                