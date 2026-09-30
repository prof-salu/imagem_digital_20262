#Bibliotecas para instalar
# pip install opencv-python numpy

# importando as biliotecas
import cv2
import numpy as np

#Importando a imagem
img = cv2.imread('sonic.jpg')

altura, largura = img.shape[:2]
dimensoes = (int(largura * 0.5), int(altura * 0.5)) #50%

#Escala
img_reduzida = cv2.resize(img, 
                          dimensoes, 
                          interpolation=cv2.INTER_AREA)

#Rotação
centro = (dimensoes[0] / 2, dimensoes[1] / 2)
matriz_rotacao = cv2.getRotationMatrix2D(center=centro,
                                         angle=45,
                                         scale=1.0)

img_rotacionada = cv2.warpAffine(src=img_reduzida, 
                                    M=matriz_rotacao,
                                    dsize=dimensoes)

#Transalação
tx, ty = 50, 0 #50 unidades em X e 0 unidades em Y

matriz_translacao = np.float32([[1, 0, tx], [0, 1, ty]])
img_translada = cv2.warpAffine(src=img_reduzida,
                               M=matriz_translacao,
                               dsize=dimensoes)


cv2.imshow('Original', img)
cv2.imshow('Reduzida', img_reduzida)
cv2.imshow('Rotacionada', img_rotacionada)
cv2.imshow('Translação', img_translada)


cv2.waitKey(0)
cv2.destroyAllWindows()