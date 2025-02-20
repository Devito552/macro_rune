import cv2
import numpy as np
import pyautogui
import time

# Função para capturar a tela inteira
def capturar_tela_inteira():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# Função para detectar movimento
def detectar_movimento(frame_atual, frame_anterior, limiar=1000):
    diff = cv2.absdiff(frame_atual, frame_anterior)  # Diferença entre os frames
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)  # Binarização
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Contornos

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > limiar:  # Área mínima para detectar movimento
            x, y, w, h = cv2.boundingRect(contorno)
            return x + w // 2, y + h // 2  # Centro do movimento
    return None

# Inicializa os frames
frame_anterior = capturar_tela_inteira()
time.sleep(1)  # Aguarda para capturar o próximo frame

# Loop principal
while True:
    frame_atual = capturar_tela_inteira()
    brilho_pos = detectar_movimento(frame_atual, frame_anterior)  # Detecta movimento

    if brilho_pos:
        print(f"Movimento detectado na posição {brilho_pos}.")
        pyautogui.moveTo(brilho_pos[0], brilho_pos[1], duration=0.3)
        time.sleep(3)
        # pyautogui.click()
    
    frame_anterior = frame_atual  # Atualiza o frame anterior
    time.sleep(3)
