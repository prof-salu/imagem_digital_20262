#Instalar as bibliotecas
#pip install numpy opencv-python

import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype=np.uint8)

#BGR
cv2.circle(img, (200, 150), 100, (0, 0, 255), -1) #vermelho
cv2.circle(img, (150, 250), 100, (255, 0, 0), -1) #Azul
cv2.circle(img, (250, 250), 100, (0, 255, 0), -1) #Verde

for x in range(3):
    canal = np.zeros((400, 400), dtype=np.uint8)
    if x == 0: cv2.circle(canal, (150, 250), 100, 255, -1) #Azul
    if x == 1: cv2.circle(canal, (250, 250), 100, 255, -1) #Verde
    if x == 2: cv2.circle(canal, (200, 150), 100, 255, -1) #Vermelho
    img[:, :, x] = canal


cv2.imshow('Sistema adtivo de cores', img)

cv2.waitKey(0)
cv2.destroyAllWindows()