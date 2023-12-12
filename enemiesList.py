import pygame
from actor import actor
import math
from anim import Animator
import projectile
from enemies import baseEnemy
from enemies import patrolling
from enemies import alerted
from enemies import patrollingRedneck
from projectile import projectileMilitia
import enemies
import sys

enemyStats = dict()
enemyStats["Health"] = {"swat": 700, "police": 100, "redneck": 25, "militia": 100, "scientist": 75, "security": 500}
enemyStats["FireRate"] = {"swat": 1, "police": 2, "redneck": 5, "militia": 2, "scientist": 1, "security": 1}
enemyStats["Speed"] = {"swat": 7, "police": 10, "redneck": 7, "militia": 15, "scientist": 7, "security": 4}
enemyStats["bulletResistance"] = {"swat": 0, "police": -1, "redneck": 0, "militia": 0, "scientist": 0, "security": 0}
enemyStats["explosionImmune"] = {"swat": True, "police": False, "redneck": False, "militia": False, "scientist": False, "security": True}
enemyStats["explosionHPloss"] = {"swat": 0, "police": 10, "redneck": 5, "militia": 5, "scientist": 5, "security": 0}
enemyStats["accuracy"] = {"swat": 0.5, "police": 0.5, "redneck": 0.1, "militia": 0.7, "scientist": 0.7, "security": 0.5}


class swat(actor): # change to enemies
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.playerStatus = enemyStatus(enemyStats, "swat")
        self.health = self.playerStatus.Health()
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
        return False

class police(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.playerStatus = enemyStatus(enemyStats, "police")
        self.health = self.playerStatus.Health()
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
        return False
        
class redneck(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.playerStatus = enemyStatus(enemyStats, "redneck")
        self.health = self.playerStatus.Health()
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
        return False

class militia(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.playerStatus = enemyStatus(enemyStats, "militia")
        self.health = self.playerStatus.Health()
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
        return False
        
class scientist(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.playerStatus = enemyStatus(enemyStats, "scientist")
        self.health = self.playerStatus.Health()
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
        return False
        

class security(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        self.angle = 0
        self.playerStatus = enemyStatus(enemyStats, "security")
        self.health = self.playerStatus.Health()
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
        return False

class enemyStatus:
    def __init__(self, enemy, enemytype):
        self.enemyStatus = enemy
        self.health = self.enemyStatus["Health"][enemytype]
        self.fireRate = self.enemyStatus["FireRate"][enemytype]
        self.speed = self.enemyStatus["Speed"][enemytype]
        self.bulletResistance = self.enemyStatus["bulletResistance"][enemytype]
        self.explosionImmune = self.enemyStatus["explosionImmune"][enemytype]
        self.explosionHPloss = self.enemyStatus["explosionHPloss"][enemytype]
        self.accuracy = self.enemyStatus["accuracy"][enemytype]

    def Health(self):
        return self.health
    
    def FireRate(self):
        return self.fireRate
    
    def Speed(self):
        return self.speed

    def BulletResistance(self):
        if self.bulletResistance < 0:
            return self.bulletResistance
        else:
            return 0

    def ExplosionImmune(self):
        if self.explosionImmune == 0:
            return self.explosionImmune
        else:
            return False
    
    def ExplosionHPloss(self):
        return self.explosionHPloss
    
    def Accuracy(self):
        return self.accuracy
    
    def updatefireRate(self):
        self.health -= 1
        if self.health < 50:
            self.fireRate += 1

""" Unused dictionary code for stats
swatStats = dict()
swatStats["health"] = 700
swatStats["fireRate"] = 1
swatStats["explosionImmune"] = True
swatStats["explosionHPloss"] = 0
swatStats["speed"] = 7
swatStats["bulletResistance"] = 0
swatStats["accuracy"] = 0.5

policeStats = dict()
policeStats["health"] = 100
policeStats["fireRate"] = 1
policeStats["explosionImmune"] = False
policeStats["explosionHPloss"] = 10
policeStats["speed"] = 10
policeStats["bulletResistance"] = -1
policeStats["accuracy"] = 0.5

redneckStats = dict()
redneckStats["health"] = 25
redneckStats["fireRate"] = 1
redneckStats["explosionImmune"] = False
redneckStats["explosionHPloss"] = 0
redneckStats["speed"] = 7
redneckStats["bulletResistance"] = 0
redneckStats["accuracy"] = 0.1

militiaStats = dict()
militiaStats["health"] = 75
militiaStats["fireRate"] = 5
militiaStats["explosionImmune"] = False
militiaStats["explosionHPloss"] = 5
militiaStats["speed"] = 20
militiaStats["bulletResistance"] = 0
militiaStats["accuracy"] = 0.7

scientistStats = dict()
scientistStats["health"] = 100
scientistStats["chemicalDamage"] = 10
scientistStats["explosionImmune"] = False
scientistStats["explosionHPloss"] = 5
scientistStats["speed"] = 7
scientistStats["bulletResistance"] = 0
scientistStats["accuracy"] = 0.7

securityStats = dict()
securityStats["health"] = 1000
securityStats["fireRate"] = 5
securityStats["explosionImmune"] = True
securityStats["explosionHPloss"] = 0
securityStats["speed"] = 4
securityStats["bulletResistance"] = 0
securityStats["accuracy"] = 0.5
"""