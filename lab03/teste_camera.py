import cv2

# Conexão com a webcam local ou stream IP do celular (ex: IP Webcam)
url = 'http://172.16.2.36:8080/video' #ip camera
#url = 0 #para acessar a webcam principal
cap = cv2.VideoCapture(url)

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

    # Exibe o frame diretamente na janela
    cv2.imshow("Visualizacao da Camera", frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()