import pygame
from actor import Player
from projectile import projectile

pygame.init()

weapon_list = ["rifle", "shotgun", "pistol", "lmg", "cyber-stick", "heavy machine gun", "wand", "knife"]
#                 0         1         2        3          4                 5              6       7

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

damage_dict = {
    "rifle" : 15,
    "shotgun" : 7,
    "pistol" : 2,
    "lmg" : 3,
    "cyber-stick" : 100,
    "heavy machine gun" : 5,
    "wand" : 50,
    "knife" : 100
}

fireRate_dict = { # x is a placeholder variable, it holds no value
    "rifle" : 1,
    "shotgun" : 1,
    "pistol" : 1,
    "lmg" : 1,
    "cyber-stick" : 1,
    "heavy machine gun" : 1,
    "wand" : 1,

}

class WeaponImage:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        return self.image

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
        self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            self.count = 0
            return True, projectile(x, y, angle)
        return False
    
    def render(self):
        pass
    
    def update(self):
        count += 1
        if self.count > self.fireRate:
            self.canFire = True

class WeaponFactory:
    def build(self, player, weapon, damage, image, ammo, fireRate, bulletRange):
        wpn = Weapon(player, weapon, damage, image, ammo, fireRate, bulletRange)
        return wpn

rifle_image = WeaponImage("rifle.png")
rifle = WeaponFactory()
rifle.build("player", weapon_list[0], damage_dict["rifle"], rifle_image, ammo_dict["rifle"], fireRate_dict["rifle"], range_dict["rifle"])
