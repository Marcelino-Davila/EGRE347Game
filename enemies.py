import pygame
from actor import actor
from anim import Animator
import math

class enemyImage():
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((200,100,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50

    def render(self,screen):
        pass
    
enemySpeed = 1
baseEnemy = enemyImage()
patrollPattern = []
patrollPattern.append((200,100)) 
patrollPattern.append((500,100))
patrollPattern.append((500,600))
patrollPattern.append((200,600))

class enemies(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
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
        self.health-=1
        if self.health < 0:
            return True
        else:
            return False

    def update(self):
        self.kinem.updateX()
        self.kinem.updateY()
        self.delgateToState(self.state.update)

class enemyState:
    def __init__(self, parent,target):
        self.parent = parent
        self.targetx, self.targety = target
        self.angle = math.atan2(self.targetx-self.parent.rect.x,self.targety-self.parent.rect.y)
    
    def update(self):
        pass

class patrolling(enemyState):
    def __init__(self,parent):
        super().__init__(parent,patrollPattern[0])
        self.patroll = patrollPattern
        self.patrollCount = 0
        self.numPatorl = len(self.patroll)
        self.target = self.patroll[self.patrollCount]
        self.targetx, self.targety = self.target
        
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

    def changeTarget(self):
        if self.patrollCount == self.numPatorl-1:
            self.patrollCount = -1
        self.patrollCount+=1
        self.target = self.patroll[self.patrollCount]
        self.targetx, self.targety = self.target

class alerted(enemyState):
    def __init__(self,parent):
        super().__init__(parent,(parent.player.rect.x,parent.player.rect.y))
        self.target = (parent.player.rect.x,parent.player.rect.y)
        self.targetx, self.targety = self.target
    
    def update(self):
        if not self.parent.alert:
            return patrolling(self.parent)
        self.angle = math.atan2(self.targetx-self.parent.rect.x,self.targety-self.parent.rect.y)
        self.parent.kinem.vel_y = enemySpeed*math.cos(self.angle)
        self.parent.kinem.vel_x = enemySpeed*math.sin(self.angle)
        self.parent.rect.x = self.parent.rect.x + self.parent.kinem.vel_x
        self.parent.rect.y = self.parent.rect.y + self.parent.kinem.vel_y
        self.target = (self.parent.player.rect.x,self.parent.player.rect.y)
        self.targetx, self.targety = self.target