import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('porcas_parafusos.jpg')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binaria = cv2.threshold(cinza, 200, 255, cv2.THRESH_BINARY_INV)

#Morfologia: fecha buracos na imagens
kernel = np.ones((5,5), np.uint8)
binaria = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, kernel, iterations=2)

#Contornos externos
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)

#Filtrar por ares
areas = [cv2.contourArea(c) for c in contornos if cv2.contourArea(c) > 500]
print(f'Objetos detectados: {len(areas)}')

#Resultados
img_resultado = img.copy()
for c in contornos:
    area = cv2.contourArea(c)
    if area < 500:
        continue

    perimetro = cv2.arcLength(c, True)
    compacidade = (4 * np.pi * area) / (perimetro ** 2) if perimetro > 0 else 0
    x, y, w, h, = cv2.boundingRect(c)
    razao_aspecto = w / h if h > 0 else 0

    cv2.drawContours(img_resultado, [c], -1, (0,0,0), 2)
    print(f'Objeto: area = {area:.0f}, compacidade = {compacidade:.3f}, aspecto = {razao_aspecto:.2f}')

cv2.imshow("Original", img)
cv2.imshow("Binaria", binaria)

cv2.waitKey(0)
cv2.destroyAllWindows()
