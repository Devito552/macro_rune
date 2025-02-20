import pyautogui
import time
import random

# Função para mover o mouse de forma mais "humana" (zigue-zague)
def movimento_humano(x, y, passos=2):
    x_atual, y_atual = pyautogui.position()
    for _ in range(passos):
        x_intermediario = random.randint(min(x_atual, x), max(x_atual, x))
        y_intermediario = random.randint(min(y_atual, y), max(y_atual, y))
        pyautogui.moveTo(x_intermediario, y_intermediario, duration=random.uniform(0.1, 0.3))
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.6))

# Função para aguardar com atraso aleatório
def espera_humana(intervalo_base):
    atraso = intervalo_base + random.uniform(-0.5, 0.5)
    time.sleep(max(0, atraso))

# Função para localizar e clicar em um ícone com tentativas
def clicar_no_icone(imagem, intervalo, tentativas=2, espera_por_tentativa=2):
    for tentativa in range(tentativas):
        pos = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
        if pos:
            x, y = pos
            x += random.randint(-3, 3)  # Adiciona variação aleatória
            y += random.randint(-3, 3)
            movimento_humano(x, y)
            pyautogui.click()
            espera_humana(intervalo)
            return True
        else:
            print(f"Tentativa {tentativa + 1} de {tentativas}: Ícone {imagem} não encontrado. Aguardando para tentar novamente...")
            time.sleep(espera_por_tentativa)
    print(f"Ícone {imagem} não foi encontrado após {tentativas} tentativas.")
    return False

# Coordenadas fixas
x1, y1 = 980, 112        # pegar lenha no banco
x2, y2 = 1278, 591       # Posicionar fora do banco
x9, y9 = 1355, 605       # Segunda posição de queima

# Tecla a ser pressionada
esc = 'esc'              # Pressionar tecla ESC

# Número de repetições
num_repeticoes = 100

# Loop com número específico de repetições
for i in range(1, num_repeticoes + 1):
    print(f"Iniciando repetição número {i}")

    # Primeira rodada de ações
    espera_humana(5)  # Espera inicial de 2 segundos
    movimento_humano(x1, y1)
    pyautogui.click()  # Pegar lenha no banco
    espera_humana(1)
    pyautogui.press(esc)
    espera_humana(2)

    movimento_humano(x2, y2)
    pyautogui.click()
    espera_humana(2)

    clicar_no_icone('icons/fm/lenha.png', 2, tentativas=3)  # Clicar na lenha
    clicar_no_icone('icons/fm/caixa.png', 4, tentativas=3)  # Caixa de fogo para acender
    clicar_no_icone('icons/fm/lenha.png', 2, tentativas=3)  # Clicar na lenha
    clicar_no_icone('icons/fm/lenhaexp.png', 100, tentativas=3)  # Adicionar lenha na fogueira
    clicar_no_icone('icons/fm/banco.png', 3, tentativas=3)  # Clicar no banco
    clicar_no_icone('icons/fm/depositar.png', 2, tentativas=3)  # Depositar itens no banco

    # Segunda rodada de ações
    movimento_humano(x1, y1)
    pyautogui.click()  # Pegar lenha no banco
    espera_humana(1)
    pyautogui.press(esc)
    espera_humana(2)

    movimento_humano(x9, y9)
    pyautogui.click()
    espera_humana(2)

    clicar_no_icone('icons/fm/lenha.png', 2, tentativas=3)  # Clicar na lenha
    clicar_no_icone('icons/fm/caixa.png', 4, tentativas=3)  # Caixa de fogo para acender
    clicar_no_icone('icons/fm/lenha.png', 2, tentativas=3)  # Clicar na lenha
    clicar_no_icone('icons/fm/lenhaexp.png', 100, tentativas=3)  # Adicionar lenha na fogueira
    clicar_no_icone('icons/fm/banco.png', 3, tentativas=3)  # Clicar no banco
    clicar_no_icone('icons/fm/depositar.png', 2, tentativas=3)  # Depositar itens no banco

    print(f"Repetição número {i} concluída")
