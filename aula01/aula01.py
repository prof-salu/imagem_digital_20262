#Instalar no terminal
#pip install numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt

#Criando um eixo de tempo (ou espaço)
x = np.linspace(0, 10, 100, 1000)

#Simulando as ondas (frequencia das cores)

#(cor: vermelho) {Menor frequencia}  [comprimento longo]
onda_vermelha = np.sin(2 * x)

#(cor: Verde) {media frequencia} [comprimento medio]
onda_verde = np.sin(3.5 * x)

#(cor: Azul) {Alta frequencia} [comprimento baixo]
onda_azul = np.sin(5 * x)

#Tamanho do grafico (inches)
plt.figure(figsize=(10,4))

#Desenha as ondas
plt.plot(x, onda_vermelha, color='red', label='Luz Vermelha')
plt.plot(x, onda_verde, color='green', label='Luz Verde')
plt.plot(x, onda_azul, color='blue', label='Luz Azul')

#Titulo da imagem
plt.title('A luz com onda')
#Aplica as legendas
plt.legend()
#Exibe a imagem
plt.show()