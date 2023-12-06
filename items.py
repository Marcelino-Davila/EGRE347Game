import pygame
from actor import Player

pygame.init()

items_list = ["meth", "shrooms", "pain-killers", "cocaine", "weed", "adderall"]

stats_list = ["damage", "move_speed", "accuracy", "hp"]

dropChance_dict = { # x is a place holder variable, it holds no value
    "meth" : x,
    "shrooms" : x,
    "pain-killers" : x,
    "cocaine" : x,
    "weed" : x,
    "adderall" : x
}

class ItemImage:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        return self.image

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

meth_image = ItemImage("meth.png")
meth_powerup = ItemFactory(player, items_list[0], meth_image, 
