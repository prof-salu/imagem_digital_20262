#Instalar as bibliotecas
#pip install numpy opencv-python

import cv2
import numpy as np

img_base = cv2.imread('super_metroid.png')

altura, largura = img_base.shape[:2]

redimensionar = 0.05

img_amostrada = cv2.resize(img_base, (0,0), fx=redimensionar, fy=redimensionar)
img_retro = cv2.resize(img_amostrada, (largura, altura), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Imagem original', img_base)
cv2.imshow('Imagem em 5%', img_amostrada)
cv2.imshow('Imagem remontada', img_retro)


cv2.waitKey(0)
cv2.destroyAllWindows()