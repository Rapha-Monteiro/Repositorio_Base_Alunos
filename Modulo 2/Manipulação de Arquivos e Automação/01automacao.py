# 1 passo: Instalar o Pyautogui com o comando: pip install pyautogui

#Crie uma automação que abra automaticamente um navegador

# importamos a bibliotec para o script em uso
import pyautogui

# 'Press' é um comando que ultilizamos para pressionar a tecla desejada
pyautogui.press('Win') # para pressionar a tecla windows 

# 'sleep' é um comando que ultilizamos para deixar o códigos 
# em espera por alguns segundos
pyautogui.sleep(1)

# 'Write' é um comando que ultilizamos para passar o que queremos
# escrever
pyautogui.write('Google Chrome ')

pyautogui.press('Enter')