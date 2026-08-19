#pip install opencv-python numpy
import cv2
import numpy as np
#1. Criar um tela de fundo preto de 400x400 pixels
#   Cores com 8 bits (1 byte) [0 - 255]
tela = np.zeros((400, 400, 3), dtype=np.uint8)
#2. Desenhando
#***ATENÇÃO ==> CV2 -> BGR****
#Vermelho
cv2.circle(tela, (200, 150), 100, (0, 0, 255), -1) 
#Verde
cv2.circle(tela, (150, 250), 100, (0, 255, 0), -1) 
#Azul
cv2.circle(tela, (250, 250), 100, (255, 0, 0), -1)

#3. Exibindo o resultado
cv2.imshow('Sistema Aditivo', tela)
cv2.waitKey(0)
cv2.destroyAllWindows()