import cv2
import numpy as np
import matplotlib.pyplot as plt

#inicia a câmera
cap = cv2.VideoCapture(0)

#Cria uma figura com dois subplots
plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

while True:
    #captura um frame
    ret, frame = cap.read()

    if not ret:
        print("Não foi possível capturar um frame")
        break

    #Converte a imagem para escala de cinza
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Converte a imagem para array
    a = np.asarray(cinza)

    #Calcula a soma das instensidades de pixels em cada coluna da imagem
    col_sum = np.sum(a, axis=0)

    #Atualiza o primeiro subplot com a img em escala de cinza
    ax1.clear()
    ax1.set_title("Da esquerda para a direita")
    ax1.imshow(cinza, cmap='gray')
    ax1.axis('off') #oculta os eixos

    #Atualiza o segundo subplot com o gráfico das somas das intensidades de pixels por coluna
    ax2.clear()
    ax2.set_title("Da esquerda para a direita")
    ax2.set_xlabel('Coluna')
    ax2.set_ylabel('Nível de claridade')
    ax2.plot(col_sum)

    #Atualiza a figura
    plt.tight_layout()
    plt.pause(0.01) #pausa para atualização da figura
    
    #Verifica se a janel foi fechada
    if plt.get_fignums() == []:
        break
#Libera a captura de vídeo e fecha as janelas
cap.release()
plt.ioff()
plt.close(fig)