


import cv2
import pyvirtualcam
import time

from face_lib import face_lib

img1 = cv2.imread('ff.jpg')
img1 = cv2.resize(img1, (200, 200))

FL = face_lib()
# Запуск видеопотока с вебкамеры
cap = cv2.VideoCapture(0)

with pyvirtualcam.Camera(width=640, height=480, fps=15) as cam:
    while True:
        ret, frame = cap.read()
        # Нахождение всех лиц на изображении
        no_of_faces, faces_coors = FL.faces_locations(frame)
        #print(faces_coors)
        if len(faces_coors) > 0:
            # Вычисление центра лица
            top, right, bottom, left =faces_coors[0]
            center_y = int((left + right) / 2)
            center_x = int((top + bottom) / 2)

            #print(center_x)

            frame = cv2.resize(frame, (640, 480))
            if center_y + img1.shape[0] < frame.shape[0] and center_x + img1.shape[1] < frame.shape[1]:
                frame[center_y:center_y+img1.shape[0], center_x:center_x+img1.shape[1]] = img1
        cam.send(frame)
        #time.sleep(0.5)

cap.release()
cv2.destroyAllWindows()
# C:\Users\p_kar\AppData\Local\Programs\Python\Python311\Lib\site-packages\face_lib\graph_final.pb

