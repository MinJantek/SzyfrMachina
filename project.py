import pygame
import random
from setup import *
from frame import Frame,Rectangle
from coders import *
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
background = pygame.image.load(f"{IMAGE_PATH}/SzyfrMachina_background.png")
lever = pygame.image.load(f"{IMAGE_PATH}/SzyfrMachina_lever.png")
picked = "frame2"
picked2 = "frame7"
font = pygame.font.SysFont("Impact",24)
active = True
frame1 = Frame((20,20),"SzyfrMachina_200.60.png","sylabowe")
frame2 = Frame((220,20),"SzyfrMachina_200.60.png","morsa")
frame3 = Frame((420,20),"SzyfrMachina_200.60.png","matematyczny")
frame4 = Frame((620,20),"SzyfrMachina_200.60.png","ulamkowy")
frame5 = Frame((820,20),"SzyfrMachina_200.60.png","komorkowy")
frame6 = Frame((1020,20),"SzyfrMachina_200.60.png","cezara")

frame7 = Frame((230,106),"SzyfrMachina_1000.300.png","")
frame8 = Frame((230,406),"SzyfrMachina_1000.300.png","")
frame9 = Frame((790,730),"SzyfrMachina_lever.png","")
sylab = Rectangle((20,80),"SzyfrMachina_sylab.png")
text1 = ""
text2 = ""
passa = False
trybe1 = ""
trybe2 = ""
while active:
    screen.blit(background,(0,0))
    if picked2 == "frame7": screen.blit(lever,(765,730))
    elif picked2 == "frame8": screen.blit(lever,(815,730))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active = False
                print(text1)
                print(text2)
            elif event.key == pygame.K_BACKSPACE:
                if picked2 == "frame8":
                    if text2:
                        text2 = text2[:-1]
                        a = endecypher(picked,picked2,text1,text2,trybe1,trybe2)
                        b = eval(f"{picked}.code_name")
                        text1 = eval(f"{b}{a}")
                elif picked2 == "frame7":
                    if text1:
                        text1 = text1[:-1]
                        a = endecypher(picked,picked2,text1,text2,trybe1,trybe2)
                        b = eval(f"{picked}.code_name")
                        text2 = eval(f"{b}{a}")
            else: 
                if picked2 == "frame8":
                    text2 += str(event.unicode)
                    a = endecypher(picked,picked2,text1,text2,trybe1,trybe2)
                    b = eval(f"{picked}.code_name")
                    text1 = eval(f"{b}{a}")
                elif picked2 == "frame7":
                    text1 += str(event.unicode)
                    a = endecypher(picked,picked2,text1,text2,trybe1,trybe2)
                    b = eval(f"{picked}.code_name")
                    text2 = eval(f"{b}{a}")
                else:
                    print(picked2)
        elif event.type == pygame.QUIT:
            active = False
            print(text1)
            print(text2)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(1,7):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())"):
                    picked = f"frame{i}"
                    if picked2 == "frame8":
                        a = endecypher(picked,picked2,text1,text2,trybe1,trybe2)
                        b = eval(f"{picked}.code_name")
                        text1 = eval(f"{b}{a}")
                    elif picked2 == "frame7":
                        a = endecypher(picked,picked2,text1,text2,trybe1,trybe2)
                        b = eval(f"{picked}.code_name")
                        text2 = eval(f"{b}{a}")
                    break   
            for i in range(7,10):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())"):
                    if i == 9 and picked2 == "frame7": i = 8
                    if i == 9 and picked2 == "frame8": i = 7
                    picked2 = f"frame{i}"
                    break
    if frame1.rect.collidepoint(pygame.mouse.get_pos()) or picked == "frame1":
        passa = True
    if sylab.isshown(passa,frame1):screen.blit(sylab.image,sylab.rect)
    else: passa = False

    for i in range(1,10):
        a = eval(f"frame{i}.render('{picked}','{picked2}','frame{i}')")
        eval(f"{a}")
    screen.blit((font.render(f"{text1}",False,(255,255,255))),(240,116))
    screen.blit((font.render(f"{text2}",False,(255,255,255))),(240,416))
    pygame.display.flip()
frame1.code_name