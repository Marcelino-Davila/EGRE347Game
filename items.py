import pygame
from actor import Player

pygame.init()

powerup_dict = { # x is a placeholder variable, it holds no value
    "meth" : x,
    "shrooms" : x,
    "pain-killers" : x,
    "cocaine" : x,
    "weed" : x,
    "adderall" : x
}

stats_list = [damage, move_speed, accuracy, hp]

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
