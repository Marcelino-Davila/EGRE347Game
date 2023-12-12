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

class MethImage:
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

class ShroomImage:
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

class PainKillerImage:
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

class CokeImage:
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

class WeedImage:
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

class AdderallImage:
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

class PowerUp:
    def __init__(self, player, statChange):
        self.player = player 
        self.statChange = statChange
        # self.statToBeChanged = statToBeChanged
    
    def changeStat(self, statToBeChanged):
        self.player.statToBeChanged += self.statChange
        return self.player.statToBeChanged

    def render(self):
        pass

# methImage = MethImage()
# shroomImage = ShroomImage()
# painkillerImage = PainKillerImage()
# cokeImage = CokeImage()
# weedImage = WeedImage()
# adderallImage = AdderallImage()

class Meth(PowerUp):
    def __init__(self, player):
        super().__init__(player, 100)
        self.image = MethImage() 

class Shrooms(PowerUp):
    def __init__(self, player):
        super().__init__(player, 50)
        self.image = ShroomImage() 

class PainKillers(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.image = PainKillerImage() 

class Cocaine(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.image = CokeImage()

class Weed(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.image = WeedImage()

class Adderall(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.image = AdderallImage()


#class ItemFactory:
#     def build(self, player, item, image, dropChance, statChange):
#         pu = PowerUp(player, item, image, dropChance, statChange)
#         pu.changeStat(statToBeChanged)
#         return pu
#
# item_image = ItemImage("item.png")
# item_powerup = ItemFactory(player, items_list[0], meth_image, dropChance_dict["item_name"], 30) 
