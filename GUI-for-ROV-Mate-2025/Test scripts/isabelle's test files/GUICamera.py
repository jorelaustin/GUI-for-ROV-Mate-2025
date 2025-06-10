import cv2
import numpy as np
import socket

def camera_feed_alt(cap):
    ret, img = cap.read()
    return img

def camera_feed(IP, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, port))
    packet, _ = sock.recvfrom(65536)
    img = cv2.imdecode(np.frombuffer(packet, dtype=np.uint8), 1)
    return img

if __name__ == "__main__":
    IP = '10.0.0.42'
    ports = [
        5005, 5006, 5007
    ]

    cap1 = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(0)
    cap3 = cv2.VideoCapture(2)
    key = 0

    while True:
        camera1 = camera_feed_alt(cap1)
        camera2 = camera_feed_alt(cap2)
        camera3 = camera_feed_alt(cap3)

        pressedKey = cv2.waitKey(1) & 0xFF
        if pressedKey != 255:
            key = pressedKey

        if key == ord('z'):
            break
        elif key == ord('2'):
            camera1 = cv2.resize(camera1, (720, 720))
            camera2 = cv2.resize(camera2, (1440,1440))
            camera3 = cv2.resize(camera3, (720,720))
            cameraDisplay = np.vstack((np.hstack((camera1, camera3)), camera2))
        elif key == ord('3'):
            camera1 = cv2.resize(camera1, (720, 720))
            camera2 = cv2.resize(camera2, (720,720))
            camera3 = cv2.resize(camera3, (1440,1440))
            cameraDisplay = np.vstack((np.hstack((camera2, camera1)), camera3))
        elif key == ord('4'):
            cameraDisplay = cv2.resize(camera1, (1800, 1800))
        elif key == ord('5'):
            cameraDisplay = cv2.resize(camera2, (1800, 1800))
        elif key == ord('6'):
            cameraDisplay = cv2.resize(camera3, (1800, 1800))
        elif key == ord('7'):
            camera1 = cv2.resize(camera1, (1080, 1080))
            camera2 = cv2.resize(camera2, (1080,1080))
            camera3 = cv2.resize(camera3, (1080,1080))
            cameraDisplay = np.hstack((np.hstack((camera1, camera2)), camera3))
        else:
            camera1 = cv2.resize(camera1, (1440, 1440))
            camera2 = cv2.resize(camera2, (720,720))
            camera3 = cv2.resize(camera3, (720,720))
            cameraDisplay = np.vstack((np.hstack((camera2, camera3)), camera1))

        cv2.imshow("Camera Feed", cameraDisplay)

    cv2.destroyAllWindows()