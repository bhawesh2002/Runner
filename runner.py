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
mud = pygame.image.load(os.path.join('Assets','tiles','5.png'))
grass = pygame.image.load(os.path.join('Assets','tiles','7.png'))
chris = pygame.image.load(os.path.join('Assets','character','chris standing.png'))
chris_scaled = pygame.transform.scale(chris,(90,130))
pixels = 128
x_pos_g = 0
while True:
    pygame.display.update()
    window.blit(chris_scaled,(150,370))
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()
    while(x_pos_g < 800):
        window.blit(ground, (x_pos_g, 500))
        x_pos_g += pixels
        if(x_pos_g > 800):
            x_pos_g = 0
            break
        pygame.display.update()
