import pygame
import math
import state
from anim import Animator

class Kinematics:
    def __init__(self, parent):
        self.parent = parent
        self.vel_x = 0
        self.vel_y = 0
        self.accel_x = 0
        self.accel_y = 0

    def updateX(self):
        self.vel_x += self.accel_x
        self.old_x = self.parent.rect.x
        self.parent.rect.x += self.vel_x     
        print(self.parent.rect.x)  

    def updateY(self):
        self.vel_y += self.accel_y 
        self.old_y = self.parent.rect.y
        self.parent.rect.y += self.vel_y

    def revertX(self):
        self.vel_x = 0
        self.parent.rect.x = self.old_x

    def revertY(self):
        self.vel_y = 0
        self.parent.rect.y = self.old_y

class Player(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.anim = Animator(color,x,y,width,height)
        self.rect = pygame.Rect(
            x,y,width, height
        )
        self.kinem = Kinematics(self)
        self.state = state.StandingState(self)

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

    def render(self,screen):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-250,y-250)*180/3.14
        img, rect = self.anim.rotate(angle)
        screen.blit(img,self.rect) 
        print(self.rect.x)   