from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        ret, frame = camera.read()
        cv2.imwrite('temp_video_feed.jpg', frame)
        yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' 
                  + open('temp_video_feed.jpg', 'rb').read() 
                  + b'\r\n') 

@app.route('/video_feed')
def video_feed():
    return Response(gen(cv2.VideoCapture(0)), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

