import cv2
import pandas as pd

# Read the data table as a string
CARP_DATA = pd.read_csv('/Users/isabelle/Desktop/MATE-Regions-main/carpData.csv',dtype=str)

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
    mapBackground = cv2.imread('./Location-of-the-Illinois-River-basin.png')
    HEIGHT, WIDTH = mapBackground.shape[:2]
    print(WIDTH)
    print(HEIGHT)

    if regionOneTruth == "Y":
        # Read the foreground image and set to the dimensions of the background
        regionOneForeground = cv2.imread('./Region 1 MAP.png')
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
        regionTwoForeground = cv2.imread('./Region 2 MAP.png')
        regionTwoForeground = cv2.resize(regionTwoForeground, (WIDTH, HEIGHT))
        regionTwoAlpha = regionTwoForeground[:, :, 2] 
        regionTwoRet, regionTwoMask = cv2.threshold(regionTwoAlpha, 10, 255, cv2.THRESH_BINARY)
        regionTwoMaskInv = cv2.bitwise_not(regionTwoMask)
        mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionTwoMaskInv)
        regionTwoForegroundMasked = cv2.bitwise_and(regionTwoForeground, regionTwoForeground, mask=regionTwoMask)
        mapBackground = cv2.add(mapBackground, regionTwoForegroundMasked)

    if (regionThreeTruth == "Y"):
        regionThreeForeground = cv2.imread('./Region 3 MAP.png')
        regionThreeForeground = cv2.resize(regionThreeForeground, (WIDTH, HEIGHT))
        regionThreeAlpha = regionThreeForeground[:, :, 2] 
        regionThreeRet, regionThreeMask = cv2.threshold(regionThreeAlpha, 10, 255, cv2.THRESH_BINARY) 
        regionThreeMaskInv = cv2.bitwise_not(regionThreeMask)
        mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionThreeMaskInv) 
        regionThreeForegroundMasked = cv2.bitwise_and(regionThreeForeground, regionThreeForeground, mask=regionThreeMask)
        mapBackground = cv2.add(mapBackground, regionThreeForegroundMasked)

    if (regionFourTruth == "Y"):
        regionFourForeground = cv2.imread('./Region 4 MAP.png')
        regionFourForeground = cv2.resize(regionFourForeground, (WIDTH, HEIGHT))
        regionFourAlpha = regionFourForeground[:, :, 2] 
        regionFourRet, regionFourMask = cv2.threshold(regionFourAlpha, 10, 255, cv2.THRESH_BINARY)
        regionFourMaskInv = cv2.bitwise_not(regionFourMask)
        mapBackground = cv2.bitwise_and(mapBackground, mapBackground, mask=regionFourMaskInv)
        regionFourForegroundMasked = cv2.bitwise_and(regionFourForeground, regionFourForeground, mask=regionFourMask)
        mapBackground = cv2.add(mapBackground, regionFourForegroundMasked)

    if (regionFiveTruth == "Y"):
        regionFiveForeground = cv2.imread('./Region 5 MAP.png')
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