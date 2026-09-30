#Bibliotecas para instalar
# pip install opencv-python numpy

# importando as biliotecas
import cv2
import numpy as np

#Importando a imagem
img = cv2.imread('placa.jpg')

#Convertando para escala de cinza
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Filtro gaussiano --> suaviza a imagem
img_suavizada = cv2.GaussianBlur(img_cinza, (5, 5), 0)

#Filtro de Média --> mascara (5,5)
img_media = cv2.blur(img_cinza, (5, 5))

#Filtro de mediana --> deve ser impar para melhor efeito
img_mediana = cv2.medianBlur(img_cinza, 5)

#Filtro Passa alta (realça bordas)
img_bordas = cv2.Canny(img_cinza, 
                       threshold1=100, 
                       threshold2=200)

#Filtro Morfologico 
#(Maxima - Clareia e expande elementos brilhantes)

kernel = np.ones((3,3), np.uint8)
img_dilatacao = cv2.dilate(img_bordas, kernel, iterations=1)

#cv2.imshow('Original', img)
cv2.imshow('Cinza', img_cinza)
cv2.imshow('Filtro Gaussiano', img_suavizada)
cv2.imshow('Media', img_media)
cv2.imshow('Mediana', img_mediana)
cv2.imshow('Bordas', img_bordas)
cv2.imshow('Dilatacao', img_dilatacao)

cv2.waitKey(0)
cv2.destroyAllWindows()