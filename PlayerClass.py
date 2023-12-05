import pygame
from actor import Player
#import weapons
import math

class playerDetection:
    def __init__(self,x,y,range):
        self.rect = pygame.Rect(
            x,y,range,range
        )
        self.image = pygame.Surface((range,range))

class soldierImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))
    
    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect) 
         

baseSoldier = soldierImage()

soldierStats = dict()
soldierStats["health"] = 100
soldierStats["speed"] = 5
soldierStats["damage"] = 10
soldierStats["detectRange"] = 300
soldierStats["accuracy"] = .5 #between 1 and 0 lower is more accurate

class soldier(Player):
    def __init__(self,x,y):
        super().__init__(x,y,baseSoldier,soldierStats)
        self.health = 100
        self.speed = 10
        #self.weapon = weapons.rifle()
        self.image = baseSoldier
        self.detectRange =playerDetection(self.rect.x+125,self.rect.y+125,soldierStats["detectRange"])

    def render(self,screen):
        self.detectRange.rect.x = self.rect.x-125
        self.detectRange.rect.y = self.rect.y-125
        screen.blit(self.detectRange.image,self.detectRange.rect)
        self.image.render(screen,self.rect.centerx,self.rect.centery,self.rect)

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

GojiraStats = dict()
GojiraStats["health"] = 200
GojiraStats["speed"] = 10
GojiraStats["damage"] = 20

class Gojira(Player):
    def __init__(self,x,y):
        super().__init__(x,y,baseGojira,GojiraStats)
        #self.weapon = weapons.rifle()
        self.image = GojiraImage()

    def __del__(self):
        return None
        