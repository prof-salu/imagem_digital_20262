#Instalar as bibliotecas
#pip install opencv-python

import cv2

img_base = cv2.imread('sonic.png')

img_cinza = cv2.cvtColor(img_base, cv2.COLOR_BGR2GRAY)
fator = 64
img_quantizada = (img_cinza // fator) * fator

cv2.imshow('Imagem Original', img_base)
cv2.imshow('Imagem Cinza', img_quantizada)

cv2.waitKey(0)
cv2.destroyAllWindows()