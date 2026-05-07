import pygame
import random
from setup import *
from frame import Frame
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
background = pygame.image.load(f"{IMAGE_PATH}/SzyfrMachina_background.png")
active = True
frame1 = Frame((0,0),"SzyfrMachina_50.50.png")
while active:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            active = False
    if frame1.rect.collidepoint(pygame.mouse.get_pos()):
        print("Antek")
        screen.blit(frame1.image,(20,20))

    
    pygame.display.flip()