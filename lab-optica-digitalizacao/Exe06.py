#Instalar as bibliotecas
#pip install opencv-python

import cv2
import numpy as np

pixel_art = np.ones((16, 16, 3), dtype=np.uint8) * 40

pixel_art[4:14, 4:12] = [0,0,0] #silhueta
pixel_art[2:4, 4:6] = [0,0,0]   #orelha esquerda
pixel_art[2:4, 10:12] = [0,0,0]   #orelha direita
pixel_art[9:12, 5:11] = [255,255,255]   #focinho (branco)
pixel_art[12:14, 7:9] = [255,255,255]   #peito (branco)
pixel_art[6:8, 5:7] = [0,255,255]   #olho esquerdo (amarelo)
pixel_art[6:8, 9:11] = [0,255,255]   #olho direito (amarelo)
pixel_art[6:8, 6] = [0,0,0]   #pupila esquerda
pixel_art[6:8, 10] = [0,0,0]   #pupila direito
pixel_art[10, 7:9] = [147,20,255]   #focinho (rosa)


gato_render = cv2.resize(pixel_art, (320, 320), 
                         interpolation=cv2.INTER_NEAREST)

cv2.imshow('Gato Pixel Art', gato_render)

cv2.waitKey(0)
cv2.destroyAllWindows()