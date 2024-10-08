## PARA RODAR O CODIGO USE O COMANDO : pip install -r requirements.txt
# OU INSTALE AS BIBLIOTECAS INDIVIDUALMENTE COM O COMANDO: pip install pygame

import pygame
pygame.init()

pygame.mixer.music.load('cortinas.mp3')
pygame.mixer.music.play()

input()
pygame.event.wait()