import cv2
import numpy as np

#Criando uma matriz de 10x10
tela = np.zeros((10, 10, 3), dtype=np.uint8)

#Manipulando os pixels individualmente
#tela[linha, coluna] = (b,g,r)
tela[0:10, 0:10] = [0, 255, 0]
tela[2, 2] = [255, 255, 255]
tela[2, 7] = [255, 255, 255]
tela[7, 2:8] = [0, 0, 255]

#Redimensionando para 300x300
imagem_ampliada = cv2.resize(tela, (300, 300),
                             interpolation=cv2.INTER_NEAREST)

cv2.imwrite('aula02/rosto.jpg', imagem_ampliada)
cv2.imshow('Manipuilação direta da matriz', imagem_ampliada)
cv2.waitKey(0)
cv2.destroyAllWindows()

