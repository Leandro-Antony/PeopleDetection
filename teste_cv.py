import cv2

# Carrega os classificadores dos Haarcascade
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
full_body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
lower_body_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

#Vídeo em tempo real
#cap = cv2.VideoCapture(0)

#aqui ele roda a img
frame = cv2.imread("pessoas1.jpeg")

#verificação da img, se encontrou ou tá corrompida 
if frame is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do arquivo.")
    exit()

font = cv2.FONT_HERSHEY_SIMPLEX
pos = (20, 50)
fontScale = 1
fontColor = (0,0,255)
thickness = 1
lineType = 2

while True:
    # Read the frame
    #frame = cap.read()#cam
    #converte a imagem para escala de cinza
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rosto e corpos
    #rosto = face_cascade.detectMultiScale(cinza, 1.1, 5)
    corpo_inteiro, _, _ = full_body_cascade.detectMultiScale3(cinza, 1.1, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE, outputRejectLevels=True)
    corpo_cima, _, _ = upper_body_cascade.detectMultiScale3(cinza, 1.1, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE, outputRejectLevels=True)
    corpo_baixo, _, _ = lower_body_cascade.detectMultiScale3(cinza, 1.1, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE, outputRejectLevels=True)

    #desenha retângulos ao redor dos objetos detectados
    #for (x, y, w, h) in rosto:
#        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    #Desenha retângulos ao redor dos corpos detectados
    for (x, y, w, h) in corpo_inteiro:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, str(len(corpo_inteiro)), pos, font, fontScale, fontColor, thickness, lineType)

    # Exibe a imagem
    cv2.imshow('IHN', frame)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
#cap.release()
cv2.destroyAllWindows()