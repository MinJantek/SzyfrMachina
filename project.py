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
frame9 = Rectangle((790,730),"SzyfrMachina_lever.png")
sylab = Rectangle((20,80),"SzyfrMachina_sylab.png")

frame10 = Frame((20,80),"SzyfrMachina_200.60.png","MALIOWEBUTY")
frame11 = Frame((20,140),"SzyfrMachina_200.60.png","NOWEBUTYLISA")
frame12 = Frame((20,200),"SzyfrMachina_200.60.png","POLITYKARENU")
frame13 = Frame((20,260),"SzyfrMachina_200.60.png","KONIECMATURY")
frame14 = Frame((20,320),"SzyfrMachina_200.60.png","MOTYLECUDAKI")
frame15 = Frame((20,380),"SzyfrMachina_200.60.png","REGULAMINOWY")
frame16 = Frame((20,440),"SzyfrMachina_200.60.png","KACEMINUTOWY")
frame17 = Frame((20,500),"SzyfrMachina_200.60.png","BITWAOCHMURY")
frame18 = Frame((20,560),"SzyfrMachina_200.60.png","HALOJUPITERY")
frame19 = Frame((20,620),"SzyfrMachina_200.60.png","AMĄNBŃCOĆÓDPERĘSFŚGTHUIWJYYKZLŹŁŻ")
frame20 = Frame((20,680),"SzyfrMachina_200.60.png","CUSTOM")
text1 = ""
text2 = ""
custom_txt = ""
passa = False
code = True 
trybe_sylab = "GADERYPOLUKI"
trybe_cezar = 0
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
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                if event.key == pygame.K_LEFT and not picked[-2].isdigit():
                    if picked != "frame1":
                        picked = f"frame{int(picked[-1])-1}"
                elif event.key == pygame.K_RIGHT:
                    if picked != "frame6" and not picked[-2].isdigit():
                        picked = f"frame{int(picked[-1])+1}"
                if not picked[-2].isdigit():
                    code_name = eval(f"{picked}.code_name")
                    if picked == "frame6":text2 = eval(f"{code_name}('{text2}',{encypher(picked2)},{trybe_cezar})")
                    elif picked == "frame1":text2 = eval(f"{code_name}('{text2}',{encypher(picked2)},'{trybe_sylab}')")
                    else:text2 = eval(f"{code_name}('{text2}',{encypher(picked2)})")
                    break   
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                if picked[-2].isdigit() or picked == "frame1":
                    if event.key == pygame.K_DOWN and picked != "frame20":
                        if picked == "frame1": picked = "frame10"
                        elif int(picked[-2]+picked[-1]) >= 10:
                            picked = picked = f"frame{int(picked[-2]+picked[-1])+1}"
                    if event.key == pygame.K_UP and picked != "frame1":
                        if picked == "frame10":picked = "frame1"
                        else:picked = picked = f"frame{int(picked[-2]+picked[-1])-1}"
                trybe_sylab = eval(f"{picked}.code_name")
                text2 = eval(f"sylabowe('{text2}',{encypher(picked2)},'{trybe_sylab}')")



            elif event.key == pygame.K_BACKSPACE:
                code_name = eval(f"{picked}.code_name")
                if picked2 == "frame8":
                    if text2: 
                        text2 = text2[:-1]
                        for i in range(10,21):
                            if f"frame{i}" == picked:
                                trybe_sylab = eval(f"{picked}.code_name")
                                print(trybe_sylab)
                                text1 = eval(f"sylabowe('{text2}',{encypher(picked2)},'{trybe_sylab}')")
                                break
                        if picked == "frame1":text1 = eval(f"{code_name}('{text2}',False,'GADERYPOLUKI')")
                        elif picked == "frame6":text1 = eval(f"{code_name}('{text2}',False,'{trybe_cezar}')")
                        elif picked == "frame2" or picked == "frame3" or picked == "frame4" or picked == "frame5":text1 = eval(f"{code_name}('{text2}',False)")
                elif picked2 == "frame7":
                    if text1: 
                        text1 = text1[:-1]
                        for i in range(10,21):
                            if f"frame{i}" == picked:
                                trybe_sylab = eval(f"{picked}.code_name")
                                print(trybe_sylab)
                                text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'{trybe_sylab}')")
                                break
                        if picked == "frame1":text2 = eval(f"{code_name}('{text1}',True,'GADERYPOLUKI')")
                        elif picked == "frame6":text2 = eval(f"{code_name}('{text1}',True,'{trybe_cezar}')")
                        elif picked == "frame2" or picked == "frame3" or picked == "frame4" or picked == "frame5":text2 = eval(f"{code_name}('{text2}',True)")
                elif picked2 == "custom":
                    if custom_txt: 
                        custom_txt = custom_txt[:-1]
            else:
                code_name = eval(f"{picked}.code_name")
                if picked2 == "frame8":
                    text2 += str(event.unicode)
                    for i in range(10,21):
                        if f"frame{i}" == picked:
                            trybe_sylab = eval(f"{picked}.code_name")
                            print(trybe_sylab)
                            text1 = eval(f"sylabowe('{text2}',{encypher(picked2)},'{trybe_sylab}')")
                            break
                    if picked == "frame1":text1 = eval(f"{code_name}('{text2}',False,'GADERYPOLUKI')")
                    elif picked == "frame6":text1 = eval(f"{code_name}('{text2}',False,'{trybe_cezar}')")
                    elif picked == "frame2" or picked == "frame3" or picked == "frame4" or picked == "frame5":text1 = eval(f"{code_name}('{text2}',False)")
                elif picked2 == "frame7":
                    text1 += str(event.unicode)
                    for i in range(10,21):
                        if f"frame{i}" == picked:
                            trybe_sylab = eval(f"{picked}.code_name")
                            print(trybe_sylab)
                            text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'{trybe_sylab}')")
                            break
                    if picked == "frame1":text2 = eval(f"{code_name}('{text1}',True,'GADERYPOLUKI')")
                    elif picked == "frame6":text2 = eval(f"{code_name}('{text1}',True,'{trybe_cezar}')")
                    elif picked == "frame2" or picked == "frame3" or picked == "frame4" or picked == "frame5":text2 = eval(f"{code_name}('{text2}',True)")
                elif picked2 == "custom":
                    custom_txt += str(event.unicode)
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
                    code_name = eval(f"{picked}.code_name")
                    if picked == "frame6":text2 = eval(f"{code_name}('{text1}',{encypher(picked2)},{trybe_cezar})")
                    elif picked == "frame1":
                        print(code_name)
                        if picked2 == "frame7":text2 = eval(f"{code_name}('{text1}',{encypher(picked2)},'GADERYPOLUKI')")
                        elif picked2 == "frame8":text1 = eval(f"{code_name}('{text2}',{encypher(picked2)},'GADERYPOLUKI')")
                    else:text2 = eval(f"{code_name}('{text1}',{encypher(picked2)})")
                    break   
            for i in range(7,10):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())"):
                    if i == 9 and picked2 == "frame7": i = 8
                    if i == 9 and picked2 == "frame8": i = 7
                    picked2 = f"frame{i}"
                    break
            for i in range(10,21):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())") and passa == True:
                    picked = f"frame{i}"
                    trybe_sylab = eval(f"{picked}.code_name")
                    if picked2 == "frame7":text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'{trybe_sylab}')")
                    else:text1 = eval(f"sylabowe('{text2}',{encypher(picked2)},'{trybe_sylab}')")

    if frame1.rect.collidepoint(pygame.mouse.get_pos()) or picked == "frame1":
        passa = True
    if sylab.isshown(passa,frame1,picked):screen.blit(sylab.image,sylab.rect)
    else: passa = False
    for i in range(1,21):
        a = eval(f"frame{i}.render('{picked}','{picked2}','frame{i}',{passa})")
        eval(f"{a}")
    screen.blit((font.render(f"{text1}",False,(255,255,255))),(240,116))
    screen.blit((font.render(f"{text2}",False,(255,255,255))),(240,416))
    pygame.display.flip()
