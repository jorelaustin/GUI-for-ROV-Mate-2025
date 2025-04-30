#import numpy as np
#import glob
import cv2

camera1 = cv2.VideoCapture(0)
counter = 0
#this is the strat, using waitKey for each if slows 
#the framerate down a ton
while True:	
	ret, frame = camera1.read()
	keyPress = cv2.waitKey(1)
	if ret:
		cv2.imshow("Live Feed", frame)
	if keyPress == ord('q'):
		cv2.destroyAllWindows()
		camera1.release()
		break
	if keyPress == ord('c'):
		counter += 1
		cv2.imshow(f"Capture {counter}", frame)
		cv2.imwrite(f"Capture_{counter}.png", frame)
		cv2.waitKey(0)
		cv2.destroyAllWindows()