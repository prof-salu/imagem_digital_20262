import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Aquisição: carregue uma imagem com objetos bem definidos sobre fundo contrastante
img = cv2.imread('pratica02.jpg')

# 2. Conversão para escala de cinza (facilita segmentação por intensidade)
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Suavização para reduzir ruído (filtro Gaussiano)
suavizada = cv2.GaussianBlur(cinza, (5, 5), 0)

# Exibindo as etapas
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')

plt.subplot(1, 3, 2)
plt.imshow(cinza, cmap='gray')
plt.title('Escala de Cinza')

plt.subplot(1, 3, 3)
plt.imshow(suavizada, cmap='gray')
plt.title('Suavizada')

plt.show()
