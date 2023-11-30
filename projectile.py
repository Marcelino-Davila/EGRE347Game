import pygame
import math
from anim import Animator
import actor

speed = 50
class projectileImage:
    def __init__(self):
        self.image = pygame.Surface((10,5))
        self.image.fill((255,0,0))
        self.image.set_colorkey((0,0,0))

    def render(self,screen,rect,angle):
        angle = (angle*180/3.14)+90
        screen.blit(pygame.transform.rotate(self.image,angle),rect)
    

baseProjectile = projectileImage()

class projectile(pygame.sprite.Sprite): 
    def __init__(self,x,y):
        super().__init__()
        self.image = baseProjectile
        self.anim = Animator(baseProjectile.image,x+25,y+25)
        self.rect = self.image.image.get_rect()
        x_mouse,y_mouse = pygame.mouse.get_pos()
        self.angle = math.atan2(x_mouse-x,y_mouse-y)
        self.kinem = actor.Kinematics(self)
        self.kinem.vel_x = -speed*math.cos(self.angle+(3.14/2))
        self.kinem.vel_y = speed*math.sin(self.angle+(3.14/2))
        self.x = x+25
        self.y = y+25

    def update(self):
        self.x = self.x + self.kinem.vel_x
        self.y = self.y + self.kinem.vel_y
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    
    def render(self,screen):
        self.image.render(screen,self.rect,self.angle)
    
    def destroy(self):
        self.kill()
