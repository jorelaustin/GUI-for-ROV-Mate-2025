# flask_camera_server.py
from flask import Flask, Response
import cv2
import threading

app = Flask(__name__)

# Initialize three camera feeds
cams = [cv2.VideoCapture(i) for i in range(3)]

def generate(camera_index):
    while True:
        success, frame = cams[camera_index].read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/cam<int:cam_id>')
def video_feed(cam_id):
    return Response(generate(cam_id), mimetype='multipart/x-mixed-replace; boundary=frame')

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
