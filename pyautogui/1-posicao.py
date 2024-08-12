# PYAUTOGUI
# No terminal: pip install pyautogui
import pyautogui as p
import time as t

t.sleep(2) # Pausa o código por 2 segundos
p.PAUSE = 3 # Pausa todos os comandos pyautogui por 3 segundos

#print(p.size()) # Tamanho da tela
print(p.position()) # Posição do mouse