import cv2
import numpy as np

# Conexão com a webcam ou stream do celular
url = 'http://172.16.2.36:8080/video'  # Use 0 para webcam padrão ou a URL do IP Webcam
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Erro: Webcam indisponível.")
    exit()

print("Pressione 'q' para sair. Aguarde a calibração inicial do fundo...")

# Captura o primeiro frame para inicializar a referência temporal
ret, frame1 = cap.read()
if not ret:
    print("Erro ao ler o primeiro frame.")
    exit()

# Pré-processamento do frame de referência
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    ret, frame2 = cap.read()
    if not ret:
    	break

    # 1. Pré-processamento do frame atual
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # 2. Subtração de Quadros: Calcula a diferença absoluta entre o frame anterior e o atual
    diferenca = cv2.absdiff(gray1, gray2)

    # 3. Limiarização (Threshold): Converte a diferença em uma máscara binária (preto e branco)
    _, thresh = cv2.threshold(diferenca, 25, 255, cv2.THRESH_BINARY)

    # 4. Dilatação da máscara para preencher pequenos buracos na silhueta em movimento
    thresh = cv2.dilate(thresh, None, iterations=2)

    # 5. Encontra os contornos das regiões que sofreram alteração
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    movimento_detectado = False

    for c in contornos:
        # Ignora pequenas variações de ruído da câmera
        if cv2.contourArea(c) < 1000:
            continue

        movimento_detectado = True

        # Desenha a caixa delimitadora (bounding box) ao redor da área de movimento
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(
            frame2, 
            "MOVIMENTO DETECTADO", 
            (x, max(y - 10, 20)), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.6, 
            (0, 0, 255), 
            2
        )

    # Status visual na tela
    status_texto = "Status: Movimento Ativo" if movimento_detectado else "Status: Ambiente Estavel"
    cor_status = (0, 0, 255) if movimento_detectado else (0, 255, 0)
    cv2.putText(frame2, status_texto, (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor_status, 2)

    # Exibição do resultado
    cv2.imshow("Diferenca (Threshold)", thresh)
    cv2.imshow("Monitoramento de Movimento", frame2)

    # Atualiza o frame de referência para o próximo ciclo temporal
    gray1 = gray2

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()