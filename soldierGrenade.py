import pygame
import math
from anim import Animator
import actor

speed =1
class grenadeImage:
    def __init__(self):
        self.image = pygame.Surface((20,20))
        self.image.fill((1,1,1))
        self.image.set_colorkey((0,0,0))

    def render(self,screen,rect):
        screen.blit(self.image,rect)

class explodeImage:
    def __init__(self):
        self.image = pygame.Surface((60,60))
        self.image.fill((200,200,0))
        self.image.set_colorkey((0,0,0))

    def render(self,screen,rect):
        rect.x-=30
        rect.y-=30
        screen.blit(self.image,rect)

baseGrenade = grenadeImage()
baseExplode = explodeImage()

class grenade(pygame.sprite.Sprite):
    def __init__(self,parent,x,y):
        super().__init__()
        self.ability = "grenade"
        mx,my = pygame.mouse.get_pos()
        self.targetx =mx-10
        self.targety =my-10
        self.kinem = actor.Kinematics(self)
        self.landed = False #True when reaches target then wait half second to explode
        self.explode = False #True when explodes then wait quarter second to delete
        self.rect = pygame.Rect(
            x+25,y+25,20,20
        )
        self.angle = math.atan2(self.targetx-self.rect.x+25,self.targety-self.rect.y+25)
        self.kinem.vel_x = -speed*math.cos(self.angle+(3.14/2))
        self.kinem.vel_y = speed*math.sin(self.angle+(3.14/2))
        self.parent = parent
        self.image = baseGrenade
        self.count = 0
        self.delete = False
        self.x = x+25
        self.y = y+25

    def update(self):
        self.x = self.x + self.kinem.vel_x
        self.y = self.y + self.kinem.vel_y
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        if (self.targetx-25 <= self.rect.x <= self.targetx+25) and (self.targety-25 <= self.rect.y <= self.targety+25):
            self.kinem.vel_x =0
            self.kinem.vel_y =0
            self.landed = True
        if self.landed:
            self.count +=1
        if self.count == 240:
            if self.count <242:
                self.rect = pygame.Rect(
                    self.rect.x-30,self.rect.y-30,60,60
                )
            self.explode = True
            self.image = baseExplode
        if self.count == 360:
            self.delete = True
            self.explode = False
    
    def render(self,screen):
        self.image.render(screen,self.rect)
