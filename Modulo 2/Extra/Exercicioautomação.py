import pyautogui
import time

time.sleep(2)
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('calc')
pyautogui.press('enter')
time.sleep(2)  
pyautogui.write('8 + 2')
pyautogui.press('enter')

