import pygame
from setup import *
import copy
class Frame(pygame.sprite.Sprite):
    def __init__(self,coordinates,file,code_name):
        super().__init__()
        self.file = file

        self.image_orginal = pygame.image.load(f"{IMAGE_PATH}/{self.file}")

        self.rect = self.image_orginal.get_rect(topleft = coordinates)
        self.code_name = code_name


    def render(self,picked,picked2,name,passa):


        self.image = copy.copy(self.image_orginal)
        #self.image = pygame.image.load(f"{IMAGE_PATH}/{self.file}")
        for i in range(10,24):
            if name == f"frame{i}" and passa == False:
                return None

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.mask = True
            if name == picked or name == picked2: self.mask = False
            if self.mask: self.image.fill((130,130,130),special_flags=pygame.BLEND_ADD)
            return f"screen.blit({name}.image,{name}.rect)"
        if name == picked or name == picked2: return f"screen.blit({name}.image,{name}.rect)"



class Rectangle(pygame.sprite.Sprite):
    def __init__(self,coordinates,file):
        super().__init__()
        self.image = pygame.image.load(f"{IMAGE_PATH}/{file}")
        self.rect = self.image.get_rect(topleft = coordinates)


    def isshown(self,passa,frame1,picked):
        for i in range(10,24):
            if picked == f"frame{i}":return True
        if picked == "frame1":return True
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if passa == True: return True
            else: return False
        else:
            if frame1.rect.collidepoint(pygame.mouse.get_pos()):
                return True
            return False
    def render(self,picked,picked2,name,passa):
        if name == picked or name == picked2: return f"screen.blit({name}.image,{name}.rect)"
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image2 = copy.copy(self.image)
            self.image2.fill((130,130,130),special_flags=pygame.BLEND_ADD)
            return f"screen.blit({name}.image2,{name}.rect)"


             
        
#pygame.image.load(f"{IMAGE_PATH}/{self.file}")
#copy.deepcopy(self.image_orginal)
        
    
    
            

