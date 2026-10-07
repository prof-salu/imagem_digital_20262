import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Aquisição: carregue uma imagem com objetos bem definidos sobre fundo contrastante
img = cv2.imread('pratica02.jpg')

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Limiarização simples (manual)
_, binaria_manual = cv2.threshold(cinza, 127, 255, cv2.THRESH_BINARY)

#Limiariazação de OTSU ()
_, binaria_otsu = cv2.threshold(cinza, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

#Limiarização adaptativa
binaria_adaptativa = cv2.adaptiveThreshold(cinza, 
                                           255, 
                                           cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, 11, 2)

#Exibindo as imagens
cv2.imshow('Original', img)
cv2.imshow('Thresold = 127', binaria_manual)
cv2.imshow('OTSU', binaria_otsu)
cv2.imshow('Adaptativa', binaria_adaptativa)

cv2.waitKey(0)
cv2.destroyAllWindows()
