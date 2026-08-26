import cv2
import os

img = cv2.imread('aula03\\anime.png')

cv2.imwrite('aula03\\anime.bmp', img) #compressão sem perda
cv2.imwrite('aula03\\anime.jpg', img) #compressão com perda
cv2.imwrite('aula03\\anime_baixa.jpg', 
            img, [cv2.IMWRITE_JPEG_QUALITY, 1]) 

print(f'Tamanho PNG: {os.path.getsize('aula03\\anime.png')}')
print(f'Tamanho BMP: {os.path.getsize('aula03\\anime.bmp')}')
print(f'Tamanho jpg: {os.path.getsize('aula03\\anime.jpg')}')
print(f'Tamanho jpg: {os.path.getsize('aula03\\anime_baixa.jpg')}')
