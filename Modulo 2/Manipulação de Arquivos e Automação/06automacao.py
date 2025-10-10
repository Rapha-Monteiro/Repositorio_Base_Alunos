import pyautogui 
import time

print("Você tem 5 segundos  para posicionar o mouse sobre o botão escrever ...")
time.sleep(5)
print("Posição do mouse", pyautogui.position())
