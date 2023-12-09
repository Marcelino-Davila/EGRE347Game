import pygame
from actor import actor
import math
from anim import Animator
import projectile
from enemies import baseEnemy
from enemies import patrolling
from enemies import alerted

class swat(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.health = 700
        self.alert = False
        self.player = player
        self.image = baseEnemy.image
        self.anim = Animator(self.image,x,y)
        self.friendlyBulltes = []
        self.state = patrolling(self)
    
    def render(self,screen):
        screen.blit(self.image, self.rect)

    def delgateToState(self, method, *args):
        new_state = method(*args)
        if new_state:
            self.state = new_state

    def collisionBullet(self):
        self.health-=1
        if self.health < 0:
            return True
        else:
            return False

    def update(self):
        self.kinem.updateX()
        self.kinem.updateY()
        self.delgateToState(self.state.update)

    def gun(self):
        return projectile.projectile(self.rect.x,self.rect.y,self.angle)
    
    def explode(self):
        self.health -= 0
        if self.health < 0:
            return True
        else:
            return False

class police(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.health = 100
        self.alert = False
        self.player = player
        self.image = baseEnemy.image
        self.anim = Animator(self.image,x,y)
        self.friendlyBulltes = []
        self.state = patrolling(self)
    
    def render(self,screen):
        screen.blit(self.image, self.rect)

    def delgateToState(self, method, *args):
        new_state = method(*args)
        if new_state:
            self.state = new_state

    def collisionBullet(self):
        self.health-=0
        if self.health < 0:
            return True
        else:
            return False

    def update(self):
        self.kinem.updateX()
        self.kinem.updateY()
        self.delgateToState(self.state.update)

    def gun(self):
        return projectile.projectile(self.rect.x,self.rect.y,self.angle)
    
    def explode(self):
        self.health -= 10
        if self.health < 0:
            return True
        else:
            return False

"""
class redneck(enemies, actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.image = pygame.Surface((50,50))
        self.health = 100
    # rednecks move faster but do not patrol

class militia(enemies, actor):
   def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.image = pygame.Surface((50,50))
        self.health = 100

class scientist(enemies, actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )

    def update(self):
        if (self.targetx-2 <= self.parent.rect.x <= self.targetx+2) and (self.targety-2 <= self.parent.rect.y <= self.targety+2):
            self.changeTarget()
        self.angle = math.atan2(self.targetx-self.parent.rect.x,self.targety-self.parent.rect.y)
        self.parent.kinem.vel_y = enemySpeed*math.cos(self.angle)
        self.parent.kinem.vel_x = enemySpeed*math.sin(self.angle)
        self.parent.rect.x = self.parent.rect.x + self.parent.kinem.vel_x
        self.parent.rect.y = self.parent.rect.y + self.parent.kinem.vel_y
        if self.parent.alert:
            return alerted(self.parent)

#class security(enemies, actor):
#   def __init__(self,x,y,player):
#        super().__init__(x,y,50,50)
#        self.rect = pygame.Rect(
#            x,y,50,50
#        )
#   security patrols faster

#if (self.jump == True): // code that is meant to kill the player if a scientist throws chemicals at them
#    self.health = 0     // technically not meant for the enemiesList

#class scientistProjectile(projectile): 
#    def __init__(self,x,y,angle):
#        super().__init__()

picture_width = self.MapImage.get_width()

movePic = 0
imagecount = math.ceil(width / picture_width) + 1

for i in range(0, imagecount):
    screen.blit(self.MapImage, (i * picture_width + movePic, 0))

movePic -= 5

if abs(movePic) > picture_width:
    movePic = 0
self.parent.rect.x

a = actor.actor()
print(a.rect.x)

#if self.parent.rect.x > 1024:
"""