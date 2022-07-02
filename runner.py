import sys
import os
import pygame
from pygame.locals import *

pygame.init()

width,height = 800,600
Black = (0,0,0)
White =( 255,255,255)
window = pygame.display.set_mode((width,height))
right_g = pygame.image.load(os.path.join('Assets','tiles','1.png'))
while True:
    window.blit(right_g,(100,100))
    window.fill(Black)
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()