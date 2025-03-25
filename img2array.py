import cv2
import numpy as np
import matplotlib.pyplot as plt #Para mostrar a imagem

#Mostra cada matriz de pixel da imagem - CUIDADO: PODE SER MUITO GRANDE
np.set_printoptions(threshold=np.inf)

#Carrega a imagem
img = cv2.imread(r'imgs\beach2.jpg')

#Converte a imagem para escala de cinza
cinza = cv2.cvtColor(Cap, cv2.COLOR_BGR2GRAY)

#Converte a imagem para array
a = np.asarray(cinza)#USA O FORMATO BGR

#Imprime a imagem em array
#print(a)

#Imprime o tamanho da imagem
print(a.shape)

# Calcula a soma das intensidades de pixels em cada coluna
col_sum = np.sum(a, axis=0)
plt.figure(figsize=(12, 6))

# Primeiro subplot: exibe a imagem em escala de cinza
plt.subplot(1, 2, 1)
plt.title('Imagem em Escala de Cinza')
plt.imshow(cinza, cmap='gray')
plt.axis('off')  # Oculta os eixos

# Segundo subplot: exibe o gráfico das somas das intensidades de pixels por coluna
plt.subplot(1, 2, 2)
plt.title('da esquerda para a direita')
plt.xlabel('Coluna')
plt.ylabel('Nível de claridade')
plt.plot(col_sum)

# Exibe a figura com os dois subplots
plt.tight_layout()
plt.show()