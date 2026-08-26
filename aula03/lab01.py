#Instalar as bibliotecas
#pip install opencv-python numpy

import cv2
import numpy as np

img = cv2.imread('aula03\\anime.png')

#Resolução espacial da imagem (Matriz)
print(f'Resolução: {img.shape}')

#Seperando os canais (bgr)
azul, verde, vermelho = cv2.split(img)

#Amostragem
#capturando apenas a altura e largura
altura, largura = img.shape[:2] 
escala_amostragem = 0.05 #5%

img_amostrada = cv2.resize(img, 
                           (0,0), 
                           fx=escala_amostragem,
                           fy=escala_amostragem)

img_reconstruida = cv2.resize(img_amostrada,
                              (largura,altura),
                              interpolation=cv2.INTER_NEAREST)

#Quantização
fator_quantizacao = 64
img_quantizada = (img // fator_quantizacao) * fator_quantizacao


cv2.imshow('Original', img)
cv2.imshow('5%', img_amostrada)
cv2.imshow('Reconstruida', img_reconstruida)
cv2.imshow('Baixa quantizacao', img_quantizada)

cv2.waitKey(0)
cv2.destroyAllWindows()