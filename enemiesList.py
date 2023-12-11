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

class swat(actor): # change to enemies
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50) # everything below this needs to be deleted
        self.rect = pygame.Rect(
            x,y,50,50
        )

class police(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )

class redneck(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )

class militia(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )

class scientist(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )

class security(actor):
    def __init__(self,x,y,player):
        super().__init__(x,y,50,50)
        self.rect = pygame.Rect(
            x,y,50,50
        )

enemyHealth = {"enemiesHealth":[{"swat": 700, "police": 100, "redneck": 25, "militia": 100, "scientist": 75, "security": 500}]}
enemyFireRate = {"enemiesFireRate":[{"swat": 700, "police": 100, "redneck": 25, "militia": 100, "scientist": 75, "security": 500}]}
enemySpeed = {"enemiesSpeed":[{"swat": 7, "police": 10, "redneck": 7, "militia": 15, "scientist": 7, "security": 7}]}

swatStats = dict()
swatStats["health"] = 700
swatStats["fireRate"] = 1
swatStats["explosionImmune"] = True
swatStats["explosionHPloss"] = 0
swatStats["speed"] = 7
swatStats["bulletResistance"] = 0

policeStats = dict()
policeStats["health"] = 100
policeStats["fireRate"] = 1
policeStats["explosionImmune"] = False
policeStats["explosionHPloss"] = 10
policeStats["speed"] = 10
policeStats["bulletResistance"] = -1

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
redneckStats["accuracy"] = 0.7

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