import sys
import os
import pygame
from pygame.locals import *

pygame.init()

width, height = 800, 600
Black = (0, 0, 0)
White = (255, 255, 255)
window = pygame.display.set_mode((width, height))
ground = pygame.image.load(os.path.join('Assets', 'tiles', '2.png'))
r_ground = pygame.image.load(os.path.join('Assets', 'tiles', '1.png'))
l_ground = pygame.image.load(os.path.join('Assets', 'tiles', '3.png'))
pixels = 128
x_pos = 0
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()
    while(x_pos < 800):
        window.blit(ground, (x_pos, 500))
        x_pos += pixels
        pygame.display.update()
    x_pos = 0
