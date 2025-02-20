import pyautogui

print("Posicione o mouse onde você deseja e pressione Enter...")
input("Pressione Enter para pegar as coordenadas do mouse...")

# Pega a posição atual do cursor
posicao = pyautogui.position()

print(f"As coordenadas do cursor são: {posicao}")

