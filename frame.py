import pygame
from setup import *

class Frame(pygame.sprite.Sprite):
    def __init__(self,coordinates,file):
        super().__init__()
        self.image = pygame.image.load(f"{IMAGE_PATH}/{file}")
        self.rect = self.image.get_rect(center = (0,0))
        self.rect = pygame.Rect(0,0,50,50)
    
    def check_collisions(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
            

