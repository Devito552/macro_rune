import pyautogui
import time
import random

# Caminho da imagem do ícone
icone = 'icons/lenha.png'

# Coordenadas fixas para os dois cliques
coordenadas_clique1 = (1276, 787)
coordenadas_clique2 = (1188, 722)

# Função para simular um movimento humano do cursor
def movimento_humano(x, y, duracao=0.5):
    pyautogui.moveTo(
        x + random.randint(-10, 10),  # Desvio aleatório no eixo X
        y + random.randint(-10, 10),  # Desvio aleatório no eixo Y
        duration=duracao + random.uniform(-0.2, 0.2)  # Duração variável
    )

# Função para verificar o ícone e realizar cliques
def verificar_e_clicar(icone, intervalo_entre_cliques=1):
    try:
        posicao = pyautogui.locateCenterOnScreen(icone)
        if posicao:
            print(f"Ícone {icone} encontrado na posição {posicao}.")
            # Realiza o primeiro clique
            movimento_humano(*coordenadas_clique1)
            pyautogui.click()
            print(f"Clique 1 realizado nas coordenadas {coordenadas_clique1}.")
            time.sleep(intervalo_entre_cliques)  # Pausa entre os cliques

            # Realiza o segundo clique
            movimento_humano(*coordenadas_clique2)
            pyautogui.click()
            print(f"Clique 2 realizado nas coordenadas {coordenadas_clique2}.")
        else:
            print(f"Ícone {icone} não encontrado na tela.")
    except pyautogui.ImageNotFoundException:
        print(f"Erro: Ícone {icone} não encontrado. Verifique o caminho da imagem e a qualidade da captura.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Loop de tentativas
tentativas = 100
for tentativa in range(1, tentativas + 1):
    print(f"Tentativa {tentativa}")
    verificar_e_clicar(icone)
    time.sleep(2)  # Pausa entre as tentativas

    # Cancela após a última tentativa
    if tentativa == tentativas:
        print("Número máximo de tentativas alcançado. Cancelando.")
        break
