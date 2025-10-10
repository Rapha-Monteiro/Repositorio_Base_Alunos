import pyautogui
import webbrowser
import time

# Passo 1: Abrir o Youtube com uma música especifica 
url = 'https://www.youtube.com/watch?v=1Ax8BWwW7jE&list=RD1Ax8BWwW7jE&start_radio=1'
webbrowser.open(url)

# Passo 2: Aguardar o carregamento da página 
time.sleep(5) # Ajustar de acordo com a velocidade da internet ultilizada

# Passo 3: Garantir que o vídeo comece (aperte o espaço para "play")
pyautogui.press('space') # toca ou pausa o vídeo
