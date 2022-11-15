import pygame
from pygame.locals import *

width = 800
height = 600

pygame.init()

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('russian roulette komrade')

pygame.display.update()

def quitter():
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT or (
             event.type == KEYDOWN and (
              event.key == K_ESCAPE or
              event.key == K_q
             )):
            pygame.quit()
            quit()

while True:
    quitter()
