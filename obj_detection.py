import cv2

#Inicializando objeto de captura
cap = cv2.VideoCapture(0)

#Definindo detector
face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
#Fonte
font = cv2.FONT_HERSHEY_COMPLEX

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
        cv2.putText(frame, str(x) +", "+ str(y), (x, y-10), font, 0.5, (0, 0, 255))

    # Exibindo o frame processado
    cv2.imshow("Object Detection", frame)

    # Tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando o objeto da webcam
cap.release()

# Destruindo janelas
cv2.destroyAllWindows()
