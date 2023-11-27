import pygame
from actor import Player

pygame.init()

class ItemImage:
    def __init__(self, image):
        self.image = pygame.image.load(image)

class PowerUp:
    def __init__(self, player, item, image, dropChance, statChange):
        self.player = player 
        self.item = item 
        self.image = image
        self.dropChance = dropChance
        self.statChange = statChange
        # self.statToBeChanged = statToBeChanged
    
    def changeStat(self, statToBeChanged):
        return self.player.statToBeChanged += self.statChange 

class ItemFactory:
    def build(self, player, item, image, dropChance, statChange, statToBeChanged):
        pu = PowerUp(player, item, image, dropChance, statChange, statToBeChanged)
        pu.changeStat(statToBeChanged)
        return pu
