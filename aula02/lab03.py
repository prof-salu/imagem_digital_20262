#pip install opencv-python numpy
import cv2
import numpy as np

#1. Carregando a imagem
imagem_django = cv2.imread('aula02\django.jpg')
imagem_batman = cv2.imread('aula02\\batman.jpg')

#2. Separando os 3 canais de cores
canal_azul, canal_verde, canal_vermelho = cv2.split(imagem_django)

#Criando imagens com apenas um canal (os outros ficam zerados)
zeros = np.zeros(canal_azul.shape[:2], dtype=np.uint8)

apenas_azul = cv2.merge([canal_azul, zeros, zeros])
apenas_verde = cv2.merge([zeros, canal_verde, zeros])
apenas_vermelho = cv2.merge([zeros, zeros, canal_vermelho])

#3. Exibindo a imagem
cv2.imshow('Original', imagem_django)
cv2.imshow('Canal Azul', apenas_azul)
cv2.imshow('Canal Verde', apenas_verde)
cv2.imshow('Canal Vermelho', apenas_verde)
cv2.imshow('Batman', imagem_batman)

cv2.waitKey(0)
cv2.destroyAllWindows()