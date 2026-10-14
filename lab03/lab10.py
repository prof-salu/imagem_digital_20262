import cv2
import numpy as np

# Conexão com a webcam ou stream do celular
url = 0 # Use 0 para webcam padrão ou a URL do IP Webcam

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Erro: Webcam indisponível.")
    exit()

# Coordenadas da Caixa Virtual (ROI): [ymin, ymax, xmin, xmax]
# Vamos definir um retângulo no terço direito superior da tela
roi_ymin, roi_ymax = 100, 300
roi_xmin, roi_xmax = 400, 600

contador = 0
objeto_dentro = False  # Flag de controle para evitar contagem contínua no mesmo frame

print("Pressione 'q' para sair. Coloque um objeto ou a mão dentro do quadrado verde...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Espelha a imagem para facilitar a interação humana
    frame = cv2.flip(frame, 1)
    
    # 1. Extração da ROI (Região de Interesse) a partir da matriz do frame
    roi = frame[roi_ymin:roi_ymax, roi_xmin:roi_xmax]

    # 2. Pré-processamento da ROI para segmentação por cor (Exemplo: Detectar tom de pele ou cor específica)
    # Convertendo para HSV para facilitar o isolamento de cores
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    # Limiares de exemplo para detecção de tom (ajuste conforme a cor do objeto desejado)
    lower_bound = np.array([35, 50, 50])   # Exemplo para tons esverdeados/gerais
    upper_bound = np.array([85, 255, 255])
    
    # Alternativa simples sem cor específica: conversão direta para escala de cinza e diferença de limiar
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_roi, 100, 255, cv2.THRESH_BINARY_INV)

    # 3. Análise de Contornos na ROI
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    movimento_na_roi = False
    for c in contornos:
        if cv2.contourArea(c) > 800: # Ignora ruídos pequenos
            movimento_na_roi = True
            break

    # 4. Lógica de Contagem Incremental (Detector de Borda de Transição)
    if movimento_na_roi and not objeto_dentro:
        contador += 1
        objeto_dentro = True  # Trava para não contar o mesmo objeto continuamente enquanto estiver parado
    elif not movimento_na_roi:
        objeto_dentro = False # Reseta a trava quando a zona estiver livre

    # 5. Interface Visual: Desenha a caixa da ROI no frame principal
    cor_caixa = (0, 0, 255) if movimento_na_roi else (0, 255, 0)
    cv2.rectangle(frame, (roi_xmin, roi_ymin), (roi_xmax, roi_ymax), cor_caixa, 3)
    
    # Exibe o status e o contador acumulado na tela
    cv2.putText(frame, f"Contador de Fluxo: {contador}", (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
    
    status_msg = "Zona Ocupada" if movimento_na_roi else "Zona Livre"
    cv2.putText(frame, status_msg, (roi_xmin, roi_ymax + 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, cor_caixa, 2)

    # Exibição do resultado
    cv2.imshow("Contador por Regiao de Interesse (ROI)", frame)
    cv2.imshow("Mascara da ROI", thresh)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()