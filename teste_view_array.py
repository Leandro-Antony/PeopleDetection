import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frame = cv2.imread("pessoa5.png")

cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

if frame is None:
        print("Não conseguiu carregar a imagem")
        break

while True:
    rosto, _, _         = face_cascade.detectMultiScale3(cinza, 1.1, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE, outputRejectLevels=True)
    a = face_cascade.read(cinza)
    print(a)
    for (x, y, w, h) in rosto:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Imagem", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()