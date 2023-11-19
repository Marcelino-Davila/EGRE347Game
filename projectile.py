import pygame
import math
from anim import Animator
import actor

speed = 50

class projectile: 
    def __init__(self,color,x,y,width,height):
        self.anim = Animator(color,x,y,width,height)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            x,y,width,height
        )
        x_mouse,y_mouse = pygame.mouse.get_pos()
        x_center,y_center = self.rect.center
        self.angle = math.atan2(x_mouse-x_center,y_mouse-y_center)
        self.kinem = actor.Kinematics(self)
        self.kinem.vel_x = -10*math.cos(self.angle+(3.14/2))
        self.kinem.vel_y = 10*math.sin(self.angle+(3.14/2))
        self.x = x
        self.y = y

    def update(self):
        self.x = self.x + self.kinem.vel_x
        self.y = self.y + self.kinem.vel_y
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    
    def render(self,screen):
        img, rect = self.anim.rotate(90+self.angle*180/3.14)
        screen.blit(img,self.rect)
    
    def destroy(self):
        pass
