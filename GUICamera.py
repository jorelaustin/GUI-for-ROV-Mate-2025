import cv2
import numpy as np

# Will need to replace external cameras with video file paths to view if no cameras are connected to laptop
cap1 = cv2.VideoCapture(0) # External camera
cap2 = cv2.VideoCapture(1) # Main camera
cap3 = cv2.VideoCapture(2) # External camera

frame1Size = 2
frame2Size = 1
frame3Size = 1

key = 0
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()

    if not ret1 or not ret2 or not ret3:
        break
    frame1Resized = cv2.resize(frame1, (frame1Size*960,frame1Size*540))
    frame2Resized = cv2.resize(frame2, (frame2Size*960,frame2Size*540))
    frame3Resized = cv2.resize(frame3, (frame3Size*960,frame3Size*540))

    if frame1Size == frame2Size:    
        numpy_vertical = np.vstack((frame1Resized, frame2Resized))
        numpy_horizontal = np.hstack((frame3, numpy_vertical))

    elif frame2Size == frame3Size:    
        numpy_vertical = np.vstack((frame2Resized, frame3Resized))
        numpy_horizontal = np.hstack((frame1, numpy_vertical))

    elif frame1Size == frame3Size:
        numpy_vertical = np.vstack((frame1Resized, frame3Resized))
        numpy_horizontal = np.hstack((frame2, numpy_vertical))
    
    pressedKey = cv2.waitKey(1) & 0xFF
    if pressedKey == ord('j'):
        frame1Size = 2
        frame2Size = 1
        frame3Size = 1
        key = 0

    elif pressedKey == ord('k'):
        frame1Size = 1
        frame2Size = 2
        frame3Size = 1
        key = 0

    elif pressedKey == ord('l'):
        frame1Size = 1
        frame2Size = 1
        frame3Size = 2
        key = 0
    elif pressedKey == ord('q'):
        break
    
    cv2.imshow("Result", numpy_horizontal)
cap1.release()
cap2.release()
cap3.release()

# Close all windows
cv2.destroyAllWindows()