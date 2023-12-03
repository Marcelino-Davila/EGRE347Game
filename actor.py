import pygame
import math
import state
from anim import Animator
from projectile import projectile

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
        self.state = state.moving(self)

    def update(self):
        self.kinem.updateX()
        self.kinem.updateY()
        
    
    def destroy(self):
        pass

class Player(actor):
    def __init__(self,x,y,width,height,image):
        super().__init__(x,y,width,height)
        self.image = image
        self.anim = Animator(self.image,x,y)
        self.friendlyBulltes = []
    
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
        for bullet in self.friendlyBulltes:
            bullet.update()

    def processMouse(self,mouse):
        left,right,middle = mouse
        if left:
            return projectile(self.rect.x,self.rect.y)

class coliders(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init()
        self.rect = pygame.Rect(
            x,y,width,height
        )
    