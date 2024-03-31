


import cv2
import pyvirtualcam
import time


img1 = cv2.imread('ff.jpg')
img1 = cv2.resize(img1, (200, 200))


# Запуск видеопотока с вебкамеры
cap = cv2.VideoCapture(0)

with pyvirtualcam.Camera(width=640, height=480, fps=60) as cam:
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 200)
        # Поиск контуров в изображении
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            
            x, y, w, h = cv2.boundingRect(contour)
    
            
            center_x = x + w // 2
            center_y = y + h // 2

            #print(center_x)

            frame = cv2.resize(frame, (640, 480))
            if center_y + img1.shape[0] < frame.shape[0] and center_x + img1.shape[1] < frame.shape[1]:
                frame[center_y:center_y+img1.shape[0], center_x:center_x+img1.shape[1]] = img1
        cam.send(frame)
        #time.sleep(0.5)

cap.release()
cv2.destroyAllWindows()

