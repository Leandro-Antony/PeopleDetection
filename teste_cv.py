import cv2

# Carrega os classificadores dos Haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

#aqui ele roda a img
img = cv2.imread("imagem3.png")

#verificação da img, se encontrou ou tá corrompida 
if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do arquivo.")
    exit()


#converte a imagem para escala de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta rosto e corpos
rosto = face_cascade.detectMultiScale(cinza, 1.3, 5)
corpo = body_cascade.detectMultiScale(cinza, 1.05, 3)

#desenha retângulos ao redor dos objetos detectados
for (x, y, w, h) in rosto:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

for (x, y, w, h) in corpo:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Exibe a imagem
cv2.imshow('IHN', img)
cv2.waitKey(0)
cv2.destroyAllWindows()