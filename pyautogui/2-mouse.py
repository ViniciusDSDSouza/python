import pyautogui as p

p.PAUSE = 0.5

# CLICAR
p.click(145, 899) # Botão Esquerdo
p.click(145, 899, button = "left", clicks = 2) # Botão Esquerdo
p.click(145, 899, button = "right", clicks = 1) # Botão Direito
p.click(145, 899, button = "middle", clicks = 2) # Botão Meio

p.moveTo(1034, 472) # Mover o mouse
p.dragTo(1919, 426, duration = 1) # Clicar e mover

p.scroll(-300) # Scroll pra baixo
p.scroll(100) # Scroll pra cima