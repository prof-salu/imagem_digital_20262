#Instalar as bibliotecas
#pip install numpy opencv-python

import cv2
import numpy as np

img_base = cv2.imread('LinkZelda.png')

if img_base is not None:
    img_sem_verde = img_base.copy()
    img_sem_verde[:, :, 1] = 0 #Zerando o canal verde
    cv2.imshow('Imagem Original', img_base)
    cv2.imshow('Imagem sem canal Verde', img_sem_verde)

cv2.waitKey(0)
cv2.destroyAllWindows()