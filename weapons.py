import pygame
from actor import Player
from projectile import projectile

pygame.init()

# weapon_list = ["rifle", "shotgun", "pistol", "lmg", "cyber-stick", "heavy machine gun", "wand", "knife"]
# #                 0         1         2        3          4                 5              6       7
#
# ammo_dict = {
#     "rifle" : 30,
#     "shotgun" : 5,
#     "pistol" : 15,
#     "lmg" : 100,
#     "cyber-stick" : 0,
#     "heavy machine gun" : 300,
#     "wand" : 10,
#     "knife" : 0
# }
#
# range_dict = {
#     "short" : 200,
#     "medium" : 400,
#     "long" : 800
# }
#
# damage_dict = {
#     "rifle" : 15,
#     "shotgun" : 7,
#     "pistol" : 2,
#     "lmg" : 3,
#     "cyber-stick" : 100,
#     "heavy machine gun" : 5,
#     "wand" : 50,
#     "knife" : 100
# }
#
# fireRate_dict = { # x is a placeholder variable, it holds no value
#     "rifle" : x,
#     "shotgun" : x,
#     "pistol" : x,
#     "lmg" : x,
#     "cyber-stick" : x,
#     "heavy machine gun" : x,
#     "wand" : x,
#
# }

class RifleImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))

    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)

class ShotgunImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))

    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)

class PistolImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))

    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)

class LMGImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))

    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)

class StickImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))

    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)

class HeavyMachineGunImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))

    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)

class WandImage:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,0,0))
        self.width = 50
        self.height = 50
        self.detectRangeI = pygame.Surface((200,200))

    def render(self,screen,x_center,y_center,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-x_center,y-y_center)*180/3.14
        screen.blit(pygame.transform.rotate(self.image,angle),rect)

# rifleImage = RifleImage()
# shotgunImage = ShotgunImage()
# pistolImage = PistolImage()
# lmgImage = LMGImage()
# stickImage = StickImage()
# heavymachineImage = HeavyMachineGunImage()
# wandImage = WandImage()

class Weapon:
    def __init__(self, damage, bulletRange):
        self.damage = damage
        self.bulletRange = bulletRange
        self.count = 0
        self.canFire = True
    
    def render(self):
        pass

class Rifle(Weapon):
    def __init__(self):
        super().__init__(10,1000)
        self.fireRate = 12
        self.count = 0
        self.canFire = True
        self.image = RifleImage()

    def update(self):
        self.count += 1
        if self.count > self.fireRate:
            self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            self.count = 0
            return projectile(x, y, angle, self.damage, self.bulletRange)


class Shotgun(Weapon):
    def __init__(self):
        super().__init__(7, 500)
        self.fireRate = 10
        self.count = 0
        self.canFire = True
        self.image = ShotgunImage()

    def update(self):
        self.count += 1
        if self.count > self.fireRate:
            self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            return projectile(x, y, angle, self.damage, self.bulletRange)


class Pistol(Weapon):
    def __init__(self):
        super().__init__(5, 500)
        self.fireRate = 10
        self.count = 0
        self.canFire = True
        self.image = PistolImage()

    def update(self):
        self.count += 1
        if self.count > self.fireRate:
            self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            return projectile(x, y, angle, self.damage, self.bulletRange)

class LMG(Weapon):
    def __init__(self):
        super().__init__(6, 1500)
        self.fireRate = 10
        self.count = 0
        self.canFire = True
        self.image = LMGImage()

    def update(self):
        self.count += 1
        if self.count > self.fireRate:
            self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            return projectile(x, y, angle, self.damage, self.bulletRange)

class Stick(Weapon):
    def __init__(self):
        super().__init__(100, 10)
        self.fireRate = 10
        self.count = 0
        self.canFire = True
        self.image = StickImage()

    def update(self):
        self.count += 1
        if self.count > self.fireRate:
            self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            return projectile(x, y, angle, self.damage, self.bulletRange)

class HeavyMachineGun(Weapon):
    def __init__(self):
        super().__init__(10,1000)
        self.fireRate = 30
        self.count = 0
        self.canFire = True
        self.image = HeavyMachineGunImage()

    def update(self):
        self.count += 1
        if self.count > self.fireRate:
            self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            self.count = 0
            return projectile(x, y, angle, self.damage, self.bulletRange)

class Wand(Weapon):
    def __init__(self):
        super().__init__(100, 50)
        self.fireRate = 10
        self.count = 0
        self.canFire = True
        self.image = WandImage()

    def update(self):
        self.count += 1
        if self.count > self.fireRate:
            self.canFire = True

    def use(self, x, y, angle):
        if self.canFire:
            self.canFire = False
            return projectile(x, y, angle, self.damage, self.bulletRange)

# class WeaponFactory:
#     def build(self, player, weapon, damage, image, ammo, fireRate, bulletRange):
#         wpn = Weapon(player, weapon, damage, image, ammo, fireRate, bulletRange)
#         return wpn
#
# rifle_image = WeaponImage("rifle.png")
# rifle = WeaponFactory()
# rifle.build(player, weapon_list[0], damage_dict["rifle"], rifle_image, ammo_dict["rifle"], fireRate_dict["rifle"], range_dict["rifle"])
