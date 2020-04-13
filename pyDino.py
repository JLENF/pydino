# created by Jairo Lenfers on 07/04/2020
# github.com/jlenf 
# based on https://github.com/angry-coder-room/auto-dino/blob/master/autoDino.py

import time
import numpy as np
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import msvcrt

keyboard = Controller()

x1_orig = 225 
x2_orig = 250 
y = 90
i = 1
diff2 = 0
start = time.time()

def pula():
    keyboard.release(Key.down)
    keyboard.press(Key.up)
    time.sleep(0.165) # 165mS para simular o tempo de uma tecla pressionada
    print('PULA')
    keyboard.release(Key.up)
    keyboard.press(Key.down)

while True:
    image = ImageGrab.grab(bbox=(40,371,800,530))
    #image.putpixel((x,y),(255,0,0));

    #image.save('C:\\Python\\1-SOURCES\\cool\\game-dino\\snapshots\\image' + str(i) +'.png');
    #i = i + 1;
    keyboard.press(Key.down)
     
    # verifica se barra de espaco foi pressionada para zerar a contagem
    if msvcrt.kbhit():
        if msvcrt.getch() == b' ':
            start = time.time()

    # cronometro
    now = time.time()
    diff = now - start

    # mostra somente uma vez cada segundo na tela
    if int(diff2) != int(diff):
        print(int(diff))
        diff2 = int(diff)
    
    # quando muda para fundo preto, pula no degrade
    if int(diff) == 60 or int(diff) == 105:
        image.putpixel((150,150),(0,0,0))
        pula()

    # quando muda para fundo branco, pula no degrade
    if int(diff) == 73:
        image.putpixel((150,150),(255,255,255))
        pula()

    # incrementa metade de cada segundo na posicao (para adequar velocidade)
    x1 = x1_orig + int(diff/2)
    x2 = x2_orig + int(diff/2)
    
    # corre um espaço entre x1 e x2 para detectar o objeto
    for x in range(x1, x2):
        # verifica qual se a cor do pixel 150x150 é preta (0,0,0)
        fundo = np.all(image.getpixel((150,150)) == (0, 0, 0), axis=-1)
        if fundo:
            # se o fundo é preto, troca a cor de detecao dos objetos
            corpixel = np.all(image.getpixel((x,y)) == (172, 172, 172), axis=-1)
        else:
            # se o fundo é branco, troca a cor de detecao dos objetos
            corpixel = np.all(image.getpixel((x,y)) == (83, 83, 83), axis=-1)

        # se detectou algum objeto, entao pula
        if corpixel:
            pula()
            break #necessario para sair do for e partir para proximo objeto