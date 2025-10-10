# Automação de login ficticio 
#Ideia : Preencher automaticamente um formúlario
#( HTML local ou simulado, via bloco de notas)

import pyautogui, time # outra maneira de escrever a importação
time.sleep(3)
pyautogui.write("aluno_python", interval=0.1)
pyautogui.press("tab")
pyautogui.write("senha123", interval=0.1)
pyautogui.press("enter")
