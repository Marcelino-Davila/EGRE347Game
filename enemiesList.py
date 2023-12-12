import pygame
from actor import actor
import math
from anim import Animator
import projectile
#from enemies import baseEnemy
#from enemies import patrolling
#from enemies import alerted
#from enemies import patrollingRedneck
from projectile import projectileMilitia
import enemies
import sys

enemyStats = dict()
enemyStats["Health"] = {"swat": 700, "police": 100, "redneck": 25, "militia": 100, "scientist": 75, "security": 500}
enemyStats["FireRate"] = {"swat": 1, "police": 2, "redneck": 5, "militia": 2, "scientist": 1, "security": 1}
enemyStats["Speed"] = {"swat": 7, "police": 10, "redneck": 7, "militia": 15, "scientist": 7, "security": 4}
enemyStats["bulletResistance"] = {"swat": 0, "police": -1, "redneck": 0, "militia": 0, "scientist": 0, "security": 0}
enemyStats["explosionImmune"] = {"swat": True, "police": False, "redneck": False, "militia": False, "scientist": False, "security": True}
enemyStats["exlposionHPloss"] = {"swat": 0, "police": 10, "redneck": 5, "militia": 5, "scientist": 5, "security": 0}
enemyStats["accuracy"] = {"swat": 0.5, "police": 0.5, "redneck": 0.1, "militia": 0.7, "scientist": 0.7, "security": 0.5}


class swat(enemies): # change to enemies
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50) # everything below this needs to be deleted
        self.rect = pygame.Rect(
            x,y,50,50
        )
        #self.parent = dict()
        #self.parent = swatStats

class police(enemies):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        #self.parent = dict()
        #self.parent = policeStats

class redneck(enemies):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        #self.parent = dict()
        #self.parent = redneckStats

class militia(enemies):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        #self.parent = dict()
        #self.parent = militiaStats

class scientist(enemies):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        #self.parent = dict()
        #self.parent = scientistStats

class security(enemies):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )
        #self.parent = dict()
        #self.parent = securityStats


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
    
    def update(self):
        self.health -= 1
        if self.health < 50:
            self.fireRate += 1
