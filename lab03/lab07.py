import cv2

# Conexão com a webcam local ou stream IP do celular (ex: IP Webcam)
url = 'http://172.16.2.36:8080/video' #ip camera
#url = 0 #para acessar a webcam principal
cap = cv2.VideoCapture(url)

#Carregando a biblioteca
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if not cap.isOpened():
    print("Erro: Webcam indisponível.")
    exit()

# Configura a janela para abrir maior e redimensionável
cv2.namedWindow("Visualizacao da Camera", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Visualizacao da Camera", 1280, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame da câmera.")
        break

    #Convertendo pra escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Classificação e reconhecimento de rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255,0,0), 2)
        cv2.putText(frame, 'Rosto', (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 0), 2)
        

    # Exibe o frame diretamente na janela
    cv2.imshow("Detecção Facial", frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()