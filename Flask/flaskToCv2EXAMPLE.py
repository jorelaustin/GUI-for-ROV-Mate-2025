import cv2

cap1 = cv2.VideoCapture('http://192.168.8.132:5050/video_feed')

while True:
    # Read frames from each camera
    ret1, frame1 = cap1.read()

    # Check if frames were successfully read
    if ret1: #and ret2:
        # Display the frames in separate windows
        cv2.imshow('Camera 1', frame1)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture objects
cap1.release()

# Close all windows
cv2.destroyAllWindows()