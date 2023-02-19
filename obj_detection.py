import cv2
import numpy as np

#Inicializando objeto que será a webcam
cap = cv2.VideoCapture(0)

#Definindo detector
face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

while True:
    # Capturando frame da webcam
    ret, frame = cap.read()

    # Descolorindo frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectando objetos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Desenhando um retângulo em volta dos objetos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Exibindo o frame processado
    cv2.imshow("Object Detection", frame)

    # Tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando o objeto da webcam
cap.release()

# Destruindo janelas
cv2.destroyAllWindows()
