import cv2
import pyvirtualcam
import time
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img1 = cv2.imread('ff.jpg')
img1 = cv2.resize(img1, (200, 200))
cap = cv2.VideoCapture(0)

with pyvirtualcam.Camera(width=640, height=480, fps=15) as cam:
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            x_offset = x + w // 2 - img1.shape[1] // 2
            y_offset = y + h // 2 - img1.shape[0] // 2
            frame = cv2.resize(frame, (640, 480))
            if y_offset + img1.shape[0] < frame.shape[0] and x_offset + img1.shape[1] < frame.shape[1]:
                frame[y_offset:y_offset+img1.shape[0], x_offset:x_offset+img1.shape[1]] = img1
        cam.send(frame)
        time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()
