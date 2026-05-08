import pygame
from setup import *
import copy
class Frame(pygame.sprite.Sprite):
    def __init__(self,coordinates,file):
        super().__init__()
        self.file = file
        self.image = pygame.image.load(f"{IMAGE_PATH}/{file}")
        self.rect = self.image.get_rect(topleft = coordinates)
    def render(self,picked,picked2,name):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = pygame.image.load(f"{IMAGE_PATH}/{self.file}")
            self.mask = True
            if name == picked or name == picked2: self.mask = False
            if self.mask: self.image.fill((130,130,130),special_flags=pygame.BLEND_ADD)
            a = f"screen.blit({name}.image,{name}.rect)"
            
            return a
        if name == picked or name == picked2: return f"screen.blit({name}.image,{name}.rect)"
        
        
         
        
    
    
            

