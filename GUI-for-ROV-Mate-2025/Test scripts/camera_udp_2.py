import cv2
import socket

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target_ip = '192.168.8.114'  # Replace with receiver IP
target_port = 5005

# Open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize and compress
    frame = cv2.resize(frame, (300, 300))
    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)
    _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])

    # UDP: Split large frames into chunks
    data = buffer.tobytes()
    #for i in range(0, len(data), 1024):
    sock.sendto(data, (target_ip, target_port))

