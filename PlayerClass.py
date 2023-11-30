import pygame
from actor import Player
import weapons
import math

class soldierImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
    
    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)  

baseSoldier = soldierImage()

class soldier(Player):
    def __init__(self,x,y):
        super().__init__(x,y,baseSoldier.width,baseSoldier.height,baseSoldier.image)
        self.health = 100
        self.speed = 10
        self.weapon = weapons.rifle()
        self.image = soldierImage()

    def __del__(self):
        return None
    

class GojiraImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,0,255))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
    
    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)  

baseGojira = GojiraImage()

class Gojira(Player):
    def __init__(self,x,y):
        super().__init__(x,y,baseSoldier.width,baseSoldier.height,baseSoldier.image)
        self.health = 100
        self.speed = 10
        self.weapon = weapons.rifle()
        self.image = GojiraImage()

    def __del__(self):
        return None
        