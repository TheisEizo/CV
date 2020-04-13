import cv2
from datetime import datetime

def findAndCaptureFaces() -> None: 
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    while True:
        ret, frame_org = cap.read()
        try: 
            frame = frame_org.copy()
        except AttributeError:
            raise AttributeError("Webcam not usable at the moment. Is it being used elsewhere?")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray)
        for n, (x,y,w,h) in enumerate(faces):
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
            face = frame_org[y:y+h,x:x+w]
            now = datetime.now().strftime('%y%m%d%H%M%S%f')
            cv2.imwrite(f'imgs/facerecheads-{n}-{now}.png',face)
        
        cv2.imshow('webcam 0',img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): #quit
            break
        elif cv2.waitKey(1) & 0xFF == ord('s'): #save img
            cv2.imwrite(f'imgs/facerecimg-{now}.png', frame_org)
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    findAndCaptureFaces()