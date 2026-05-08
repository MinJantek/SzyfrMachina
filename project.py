import pygame
import random
from setup import *
from frame import Frame
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
background = pygame.image.load(f"{IMAGE_PATH}/SzyfrMachina_background.png")
picked = "frame2"
picked2 = "frame7"
active = True
frame1 = Frame((20,20),"SzyfrMachina_200.60.png")
frame2 = Frame((220,20),"SzyfrMachina_200.60.png")
frame3 = Frame((420,20),"SzyfrMachina_200.60.png")
frame4 = Frame((620,20),"SzyfrMachina_200.60.png")
frame5 = Frame((820,20),"SzyfrMachina_200.60.png")
frame6 = Frame((1020,20),"SzyfrMachina_200.60.png")

frame7 = Frame((230,106),"SzyfrMachina_1000.300.png")
frame8 = Frame((230,406),"SzyfrMachina_1000.300.png")
while active:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active = False
                print("________tekst szyfru_______")
                print("________tekst szyfru_______")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(1,7):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())"):
                    picked = f"frame{i}"
                    print("ANTEk")
                    break
            for i in range(7,9):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())"):
                    picked2 = f"frame{i}"
                    print("ANTEkkkkkk")
                    break
    for i in range(1,9):
        a = eval(f"frame{i}.render('{picked}','{picked2}','frame{i}')")
        eval(f"{a}")


    
    pygame.display.flip()