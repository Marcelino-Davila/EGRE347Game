import pygame
from actor import Player

pygame.init()

# items_list = ["meth", "shrooms", "pain-killers", "cocaine", "weed", "adderall"]
#
# stats_list = ["damage", "move_speed", "accuracy", "hp"]
#
# dropChance_dict = { # x is a place holder variable, it holds no value
#     "meth" : x,
#     "shrooms" : x,
#     "pain-killers" : x,
#     "cocaine" : x,
#     "weed" : x,
#     "adderall" : x
# }

class ItemImage:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        return self.image

class PowerUp:
    def __init__(self, player, image, statChange):
        self.player = player 
        self.image = image
        self.statChange = statChange
        # self.statToBeChanged = statToBeChanged
    
    def changeStat(self, statToBeChanged):
        self.player.statToBeChanged += self.statChange
        return self.player.statToBeChanged

    def render(self):
        pass

class Meth(PowerUp):
    def __init__(self):
        super().__init__(player, meth_image, 100)

    def changeStat(self):
        pass

class Shrooms(PowerUp):
    def __init__(self):
        super().__init__()

    def changeStat(self):
        pass

class PainKillers(PowerUp):
    def __init__(self):
        super().__init__()

    def changeStat(self):
        pass

class Cocaine(PowerUp):
    def __init__(self):
        super().__init__()

    def changeStat(self):
        pass 

class Weed(PowerUp):
    def __init__(self):
        super().__init__()

    def changeStat(self):
        pass 

class Adderall(PowerUp):
    def __init__(self):
        super().__init__()

    def changeStat(self):
        pass 


#class ItemFactory:
#     def build(self, player, item, image, dropChance, statChange):
#         pu = PowerUp(player, item, image, dropChance, statChange)
#         pu.changeStat(statToBeChanged)
#         return pu
#
# item_image = ItemImage("item.png")
# item_powerup = ItemFactory(player, items_list[0], meth_image, dropChance_dict["item_name"], 30) 
