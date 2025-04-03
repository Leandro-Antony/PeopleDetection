from ultralytics import YOLO
import cv2

#Carrega um modelo
modelo = YOLO("yolo11n.pt")

#Inicia a captura de vídeo
cap = cv2.VideoCapture(0)

#Verifica se a câmera foi inicializada corretamente
if not cap.isOpened():
    print("Não foi possível inicializar a câmera")
    exit()

while True:
    ret, frame = cap.read()
    
    #Realiza a detecção de objetos no frame atual
    resultados = modelo(frame)

    n_pessoas = len(resultados[0].data)
    print("Número de pessoas detectadas:", n_pessoas)

    #Desenha as detecções no frame
    frame_desenhado = resultados[0].plot()

    #Exibe o frame com as detecções
    cv2.imshow("Detecção de pessoas", frame_desenhado)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

#Fecha a câmera e as janelas
cap.release()  
cv2.destroyAllWindows()