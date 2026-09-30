#Bibliotecas para instalar
# pip install opencv-python numpy

# importando as biliotecas
import cv2
import numpy as np

#Importando a imagem
img = cv2.imread('resident_evil.jpg')

#Definindo o valor a ser aplicado
matriz_brilho = np.ones(img.shape, dtype='uint8') * 80

#Aumentando o brilho (+80)
img_clara = cv2.add(img, matriz_brilho)

#Diminuindo o brilho (-80)
img_escura = cv2.subtract(img, matriz_brilho)

cv2.imshow('Original', img)
cv2.imshow('Clareamento', img_clara)
cv2.imshow('Escurecendo', img_escura)

cv2.waitKey(0)
cv2.destroyAllWindows()