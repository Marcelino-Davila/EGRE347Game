import pygame
import math
import state
import random
from anim import Animator
from projectile import projectile
import soldierGrenade

class Kinematics:
    def __init__(self, parent):
        self.parent = parent
        self.vel_x = 0
        self.vel_y = 0

    def updateX(self):
        self.old_x = self.parent.rect.x
        self.parent.rect.x += self.vel_x     

    def updateY(self): 
        self.old_y = self.parent.rect.y
        self.parent.rect.y += self.vel_y

    def revertX(self):
        self.vel_x = 0
        self.parent.rect.x = self.old_x

    def revertY(self):
        self.vel_y = 0
        self.parent.rect.y = self.old_y

class actor(pygame.sprite.Sprite):
    def __init__(self,x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(
            x,y,width, height
        )
        self.kinem = Kinematics(self)

    def update(self):
        self.kinem.updateX()
        self.kinem.updateY() 

class Player(actor):
    def __init__(self,x,y,image,stats):
        super().__init__(x,y,image.width,image.height)
        self.image = image.image
        self.anim = Animator(self.image,x,y)
        self.friendlyBulltes = []
        self.state = state.moving(self,stats["speed"])
        self.accuracy = stats["accuracy"]
        self.ability = False

    def delgateToState(self, method, *args):
        new_state = method(*args)
        if new_state:
            self.state = new_state

    def processInput(self, pressed):
        self.delgateToState(self.state.processInput, pressed)

    def update(self):
        self.kinem.updateX()
        self.kinem.updateY()
        self.delgateToState(self.state.update)
        self.classAbility()

    def processMouse(self,mouse):
        left,right,middle = mouse
        if left:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            recoil = (random.randrange(-100,100)/100)*0.261799*self.accuracy
            angle = math.atan2(x_mouse-self.rect.x+25,y_mouse-self.rect.y+25) + recoil
            return projectile(self.rect.x,self.rect.y,angle)
        
    def collisionBullet(self):
        self.health-=1
        if self.health < 0:
            return True
        else:
            return False
    
    def classAbility(self):
        return soldierGrenade.grenade(self,self.rect.x,self.rect.y)  

class coliders(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,width=0,height=0):
        super().__init__()
        self.rect = pygame.Rect(
            x,y,width,height
        )
        self.image = pygame.Surface((width,height))
        self.image.fill((50,50,50))

    def update(self):
        pass 

    def render(self,screen):
        screen.blit(self.image,self.rect)