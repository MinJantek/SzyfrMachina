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
active = True
font =pygame.font.SysFont("",30)
frame1 = Frame((20,20),"SzyfrMachina_200.60.png","sylabowe")
frame2 = Frame((220,20),"SzyfrMachina_200.60.png","morsa")
frame3 = Frame((420,20),"SzyfrMachina_200.60.png","matematyczny")
frame4 = Frame((620,20),"SzyfrMachina_200.60.png","ulamkowy")
frame5 = Frame((820,20),"SzyfrMachina_200.60.png","komorkowy")
frame6 = Frame((1020,20),"SzyfrMachina_50.50.png","cezara")

frame7 = Frame((230,106),"SzyfrMachina_1000.300.png","")
frame8 = Frame((230,406),"SzyfrMachina_1000.300.png","")
frame9 = Rectangle((790,730),"SzyfrMachina_lever.png")
sylab = Rectangle((20,80),"SzyfrMachina_sylab.png")
clear = Rectangle((1130,700),"SzyfrMachina_clear.png")
custom = Rectangle((20,740),"SzyfrMachina_200.50.png")
up = Rectangle((1195,20),"SzyfrMachina_26.16.png")
down = Rectangle((1195,64),"SzyfrMachina_26.16.png")
number = Rectangle((1195,38),"SzyfrMachina_26.16.png")

frame10 = Frame((20,80),"SzyfrMachina_200.60.png","MALIOWEBUTY")
frame11 = Frame((20,140),"SzyfrMachina_200.60.png","NOWEBUTYLISA")
frame12 = Frame((20,200),"SzyfrMachina_200.60.png","POLITYKARENU")
frame13 = Frame((20,260),"SzyfrMachina_200.60.png","KONIECMATURY")
frame14 = Frame((20,320),"SzyfrMachina_200.60.png","MOTYLECUDAKI")
frame15 = Frame((20,380),"SzyfrMachina_200.60.png","REGULAMINOWY")
frame16 = Frame((20,440),"SzyfrMachina_200.60.png","KACEMINUTOWY")
frame17 = Frame((20,500),"SzyfrMachina_200.60.png","BITWAOCHMURY")
frame18 = Frame((20,560),"SzyfrMachina_200.60.png","HALOJUPITERY")
frame19 = Frame((20,620),"SzyfrMachina_200.60.png","AMĄNBŃCOĆÓDPERĘSFŚGTHUIWJYKZLŹŁŻ")
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
    if clear.rect.collidepoint(pygame.mouse.get_pos()):screen.blit(clear.image,clear.rect)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active = False
                print(text1)
                print("--------------------")
                nazwa = eval(f"{picked}.code_name")
                if nazwa.upper() == "CUSTOM":nazwa = custom_txt
                if nazwa == "cezar": nazwa = f"cezar: {trybe_cezar}"
                print(nazwa)
                print("--------------------")
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
            elif event.key == pygame.K_RETURN:
                if picked2 == "frame7":text1 += " "
                elif picked2 == "frame8":text2 += " "
            elif event.key == pygame.K_BACKSPACE:
                code_name = eval(f"{picked}.code_name")
                if picked2 == "frame8":
                    if text2: 
                        text2 = text2[:-1]
                        for i in range(10,21):
                            if f"frame{i}" == picked:
                                trybe_sylab = eval(f"{picked}.code_name")
                                if trybe_sylab == "CUSTOM":
                                    if custom_txt:trybe_sylab = custom_txt
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
                                if trybe_sylab == "CUSTOM":
                                    if custom_txt:trybe_sylab = custom_txt
                                text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'{trybe_sylab}')")
                                break
                        if picked == "frame1":text2 = eval(f"{code_name}('{text1}',True,'GADERYPOLUKI')")
                        elif picked == "frame6":text2 = eval(f"{code_name}('{text1}',True,'{trybe_cezar}')")
                        elif picked == "frame2" or picked == "frame3" or picked == "frame4" or picked == "frame5":text2 = eval(f"{code_name}('{text1}',True)")
                elif picked2 == "custom":
                    if custom_txt:custom_txt = custom_txt[:-1]
                elif picked2 == "number":
                    trybe_cezar = str(trybe_cezar)[:-1]
                    if trybe_cezar and trybe_cezar != "-":trybe_cezar = int(trybe_cezar)
                    elif not trybe_cezar: trybe_cezar = 0
            else:
                code_name = eval(f"{picked}.code_name")
                if picked2 == "frame8":
                    text2 += str(event.unicode)
                    for i in range(10,21):
                        if f"frame{i}" == picked:
                            trybe_sylab = eval(f"{picked}.code_name")
                            if trybe_sylab == "CUSTOM":
                                if custom_txt:trybe_sylab = custom_txt
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
                            if trybe_sylab == "CUSTOM":
                                if custom_txt:trybe_sylab = custom_txt
                            text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'{trybe_sylab}')")
                            break
                    if picked == "frame1":text2 = eval(f"{code_name}('{text1}',True,'GADERYPOLUKI')")
                    elif picked == "frame6":text2 = eval(f"{code_name}('{text1}',True,'{trybe_cezar}')")
                    elif picked == "frame2" or picked == "frame3" or picked == "frame4" or picked == "frame5":
                            text2 = eval(f"{code_name}('{text1}',True)")
                elif picked2 == "custom":custom_txt += str(event.unicode).upper()
                elif picked2 == "number":
                    if not trybe_cezar:
                        if event.unicode == "-":trybe_cezar = "-"
                        else:trybe_cezar = int(str(trybe_cezar)+event.unicode)
                    else:trybe_cezar = int(str(trybe_cezar)+event.unicode)
        elif event.type == pygame.QUIT:
            active = False
            print(text1)
            print("--------------------")
            nazwa = eval(f"{picked}.code_name")
            if nazwa.upper() == "CUSTOM":nazwa = custom_txt
            if nazwa == "cezara": nazwa = f"cezara: {trybe_cezar}"
            print(nazwa)
            print("--------------------")
            print(text2)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(2,6):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())"):
                    picked = f"frame{i}"
                    code_name = eval(f"{picked}.code_name")
                    if picked == "frame6":text2 = eval(f"{code_name}('{text1}',{encypher(picked2)},{trybe_cezar})")
                    elif picked == "frame1":
                        print(code_name)
                        if picked2 == "frame7":text2 = eval(f"{code_name}('{text1}',{encypher(picked2)},'GADERYPOLUKI')")
                        elif picked2 == "frame8":text1 = eval(f"{code_name}('{text2}',{encypher(picked2)},'GADERYPOLUKI')")
                    elif picked == "frame1":text2 = eval(f"{code_name}('{text1}',{encypher(picked2)},'GADERYPOLUKI')")

                    else:text2 = eval(f"{code_name}('{text1}',{encypher(picked2)})")
                    break   
            for i in range(7,10):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())"):
                    if i == 9 and picked2 == "frame7": i = 8
                    elif i == 9 and picked2 == "frame8": i = 7
                    elif i == 9: i = 7
                    picked2 = f"frame{i}"
                    if picked == "frame6":
                        print(picked2)
                        if picked2 == "frame7":text2 = cezara(text1,True,trybe_cezar)
                        elif picked2 == "frame8":text1 = cezara(text2,False,trybe_cezar)

                    break
            for i in range(10,21):
                if eval(f"frame{i}.rect.collidepoint(pygame.mouse.get_pos())") and passa == True:
                    done = False
                    before = picked
                    picked = f"frame{i}"
                    code_name = eval(f"{picked}.code_name")
                    if code_name == "CUSTOM":
                                if custom_txt:code_name = custom_txt
                    for b in range(10,21):
                        if before == f"frame{b}" or before == "frame1" or before == "frame6":
                            if picked2 == "frame7":text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'{code_name}')")
                            elif picked2 == "frame8":text1 = eval(f"sylabowe('{text2}',{encypher(picked2)},'{code_name}')")
                            done = True
                            break
                    if not done:text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'{code_name}')")
            if frame1.rect.collidepoint(pygame.mouse.get_pos()):
                done = False
                before = picked
                picked = "frame1"
                for b in range(10,21):
                    done = False
                    if before == f"frame{b}" or before == "frame1" or before == "frame6":
                        if picked2 == "frame7":text2 = eval(f"sylabowe('{text1}',{encypher(picked2)},'GADERYPOLUKI')")
                        elif picked2 == "frame8":text1 = eval(f"sylabowe('{text2}',{encypher(picked2)},'GADERYPOLUKI')")
                        done = True
                if not done:text2 = sylabowe(text1,encypher(picked2),'GADERYPOLUKI')
            elif frame6.rect.collidepoint(pygame.mouse.get_pos()):
                done = False
                before = picked
                picked = "frame6"
                for b in range(10,21):
                    if before == f"frame{b}" or before == "frame1" or before == "frame6":
                        if picked2 == "frame7":text2 = eval(f"cezara('{text1}',True,{trybe_cezar})")
                        elif picked2 == "frame8":text1 = eval(f"cezara('{text2}',False,{trybe_cezar})")
                        done = True
                        print(before)
                        break
                if not done:
                    text2 = cezara(text1,encypher(picked2),trybe_cezar)
            elif clear.rect.collidepoint(pygame.mouse.get_pos()):
                text1 = ""
                text2 = ""
                custom_txt = ""
            elif custom.rect.collidepoint(pygame.mouse.get_pos()):picked2 = "custom"
            elif up.rect.collidepoint(pygame.mouse.get_pos()):
                print(isinstance(trybe_cezar,int))
                trybe_cezar += 1
                if picked2 == "frame7":text2 = cezara(text1,True,trybe_cezar)
                elif picked2 == "frame8":text1 = eval(f"cezara('{text2}',False,{trybe_cezar})")
            elif down.rect.collidepoint(pygame.mouse.get_pos()):
                print(isinstance(trybe_cezar,int))
                trybe_cezar -= 1
                if picked2 == "frame7":text2 = eval(f"cezara('{text1}',True,{trybe_cezar})")
                elif picked2 == "frame8":text1 = eval(f"cezara('{text2}',False,{trybe_cezar})")
            elif number.rect.collidepoint(pygame.mouse.get_pos()):picked2 = "number"
    if frame1.rect.collidepoint(pygame.mouse.get_pos()) or picked == "frame1":
        passa = True
    if sylab.isshown(passa,frame1,picked):screen.blit(sylab.image,sylab.rect)
    else: passa = False
    for i in range(1,21):
        a = eval(f"frame{i}.render('{picked}','{picked2}','frame{i}',{passa})")
        eval(f"{a}")
    eval(f"[{custom.render(picked,picked2,'custom',{passa})}]")
    eval(f"[{up.render(picked,picked2,'up',{passa})}]")
    eval(f"[{down.render(picked,picked2,'down',{passa})}]")

    eval(f"[{number.render(picked,picked2,'number',{passa})}]")
    #tekst linijki - text1[int(i//srednia1):int((i+pixele_tekstu)//srednia1)]
    #ilość linijek - font.size(text1)[0]/pixele_tekstu
    font =pygame.font.SysFont("",25)
    screen.blit(font.render(str(trybe_cezar),False,(0,0,0)),(1207.5-font.size(str(trybe_cezar))[0]/2,43))
    font =pygame.font.SysFont("",30)
    screen.blit(font.render(custom_txt,False,(255,255,255)),(30,745))
    srednia1 = font.size(text1)[0]/len(text1) if text1 else 0
    srednia2 = font.size(text2)[0]/len(text2) if text2 else 0
    for i in range(0,font.size(str(text1))[0],pixele_tekstu):
        screen.blit(font.render(text1[int(i//srednia1):int((i+pixele_tekstu)//srednia1)],False,(255,255,255)),(240,116+i/pixele_tekstu*font.size(text1)[1]))
    for i in range(0,font.size(str(text2))[0],pixele_tekstu):
        screen.blit(font.render(text2[int(i//srednia2):int((i+pixele_tekstu)//srednia2)],False,(255,255,255)),(240,416+i/pixele_tekstu*font.size(text2)[1]))
    pygame.display.flip()

screen.blit(font.render(text1,False,(255,255,255)),(240,116))