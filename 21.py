# Tocando um MP3
import time

import pygame
pygame.init()
pygame.mixer.music.load('21.mp3')
pygame.mixer.music.play()
pygame.event.wait() # Não ta funcando
parar = input('Digite para parar') # Gambiarra

# import time
# time.sleep(360)