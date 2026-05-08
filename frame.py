import pygame
from setup import *

class Frame(pygame.sprite.Sprite):
    def __init__(self,coordinates,file,code_name):
        super().__init__()
        self.file = file
        self.image = pygame.image.load(f"{IMAGE_PATH}/{file}")
        self.rect = self.image.get_rect(topleft = coordinates)
        self.code_name = code_name
    def render(self,picked,picked2,name):
        self.image = pygame.image.load(f"{IMAGE_PATH}/{self.file}")
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.mask = True
            if name == picked or name == picked2: self.mask = False
            if self.mask: self.image.fill((130,130,130),special_flags=pygame.BLEND_ADD)
            a = f"screen.blit({name}.image,{name}.rect)"
            return a
        if name == picked or name == picked2: return f"screen.blit({name}.image,{name}.rect)"
        
        
         
        
    
    
            

