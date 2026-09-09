#Instalar as bibliotecas
#pip install opencv-python

import cv2
import numpy as np

espelho = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.line(espelho, (150, 0), (150, 300), (255, 255, 255), 2)# linha branca
cv2.line(espelho, (0,0), (150, 150), (0, 255, 255), 4) #raio

cv2.imshow('Raio', espelho)

lado_esquerdo = espelho[:, 0: 150]
reflexao = cv2.flip(lado_esquerdo, 1)
espelho[:, 150:300] = reflexao

cv2.imshow('Imagem espelhada', espelho)


cv2.waitKey(0)
cv2.destroyAllWindows()