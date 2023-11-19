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
    
    def __init__(self, color, x, y, width, height,weapon=0):
        super().__init__()
        self.anim = Animator(color,x,y,width,height)
        self.rect = pygame.Rect(
            x,y,width, height
        )
        self.kinem = Kinematics(self)
        self.state = state.moving(self)
        self.weapon = weapon

    def update(self):
        self.kinem.updateX()
        self.kinem.updateY()
        
    
    def destroy(self):
        pass

class Player(actor):
    def __init__(self,color,x,y,width,height):
        super().__init__(color,x,y,width,height)
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

    def gun(self):
        self.friendlyBulltes.append(projectile((255,0,0),self.rect.x,self.rect.y,50,10))

    def render(self,screen):
        x,y = pygame.mouse.get_pos()
        x_center,y_center = self.rect.center
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        img, rect = self.anim.rotate(angle)
        screen.blit(img,self.rect) 
        for bullet in self.friendlyBulltes:
            bullet.render(screen)
    