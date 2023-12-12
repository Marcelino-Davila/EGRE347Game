import pygame
from actor import Player
import weapons
import math
import soldierGrenade
import lazer
import pygame.locals as keys


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
soldierStats["health"] = 5000
soldierStats["speed"] = 5
soldierStats["damage"] = 10
soldierStats["detectRange"] = 300
soldierStats["accuracy"] = .5 #between 1 and 0 lower is more accurate

class soldier(Player):
    def __init__(self,x,y):
        super().__init__(x,y,baseSoldier,soldierStats)
        self.grenadeCD = 0
        self.health = soldierStats["health"]
        self.speed = soldierStats["speed"]
        self.weapon = weapons.Rifle()
        self.image = baseSoldier
        self.detectRange =playerDetection(self.rect.x+125,self.rect.y+125,soldierStats["detectRange"])
        self.WallCollide = True
        self.grenadeCoord = (0,0)
        self.jump = False

    def render(self,screen):
        self.grenadeCD-=1
        self.detectRange.rect.x = self.rect.x-125
        self.detectRange.rect.y = self.rect.y-125
        #screen.blit(self.detectRange.image,self.detectRange.rect)
        self.image.render(screen,self.rect.centerx,self.rect.centery,self.rect)

    def rocketJump(self,explode):
        self.jump = True
        self.grenadeCoord = explode

    def classAbility(self):
        print(self.grenadeCD)
        if self. ability and self.grenadeCD < 0:
            self.grenadeCD = 100 
            return soldierGrenade.grenade(self,self.rect.x,self.rect.y) 

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
GojiraStats["health"] = 10000
GojiraStats["speed"] = 7
GojiraStats["damage"] = 10
GojiraStats["detectRange"] = 150
GojiraStats["accuracy"] = .1 #between 1 and 0 lower is more accurate

class Gojira(Player):
    def __init__(self,x,y):
        super().__init__(x,y,baseGojira,GojiraStats)
        self.weapon = weapons.Rifle()
        self.image = GojiraImage()
        self.detectRange =playerDetection(self.rect.x+125,self.rect.y+125,GojiraStats["detectRange"])
        self.rocketJump = False
        self.health = GojiraStats["health"]
        self.jump = False
        self.Lazer = False
        self.ability = False
        
    def render(self,screen):
        self.detectRange.rect.x = self.rect.x-50
        self.detectRange.rect.y = self.rect.y-50
        #screen.blit(self.detectRange.image,self.detectRange.rect)
        self.image.render(screen,self.rect.centerx,self.rect.centery,self.rect)
    
    def classAbility(self):
        if self.ability:
            return lazer.lazerBeams(self)