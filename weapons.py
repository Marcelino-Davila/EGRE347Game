import pygame
from actor import Player

pygame.init()

ammo_dict = {
    "rifle" : 30,
    "shotgun" : 5,
    "pistol" : 15,
    "lmg" : 100,
    "cyber-stick" : 0,
    "heavy machine gun" : 300,
    "wand" : 10,
    "knife" : 0
}

range_dict = {
    "short" : 200,
    "medium" : 400,
    "long" : 800
}

class WeaponLoad:
    def __init__(self, image):
        self.image = pygame.image.load(image)

class Weapon:
    def __init__(self, player, weapon, damage, image, ammoCount, ammoLoss, fireRate, bulletRange):
        self.player = player
        self.weapon = weapon
        self.damage = damage
        self.image = image
        self.ammoCount = ammoCount
        self.ammoLoss = ammoLoss
        self.fireRate = fireRate
        self.bulletRange = bulletRange
        self.count = 0

    def use(self):
        
        return bullet
    
    def render(self):
        pass
    
    def update(self):
        fireRate += 1

class WeaponFactory:
    def build(self, player, weapon, damage, image, ammo, fireRate, bulletRange):
        wpn = Weapon(player, weapon, damage, image, ammo, fireRate, bulletRange)
        return wpn

rifle = WeaponFactory()
rifle.build("player", "rifle", "rifle.png", 30, 15, medium)
