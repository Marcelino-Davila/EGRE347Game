import pygame
from actor import Player

pygame.init()

class WeaponLoad:
    def __init__(self, image):
        self.image = pygame.image.load(image)

class Weapon:
    def __init__(self, player, weapon, image, ammoCount, ammoLoss, fireRate, bulletRange):
        self.player = player
        self.weapon = weapon
        self.image = image
        self.ammoCount = ammoCount
        self.ammoLoss = ammoLoss
        self.fireRate = fireRate
        self.bulletRange = bulletRange

    def use(self):
         

class WeaponFactory:
    def build(self, player, weapon, image, ammo, fireRate, bulletRange):
        wpn = Weapon(player, weapon, image, ammo, fireRate, bulletRange)
        return wpn
