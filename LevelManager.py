import pygame
import json


def MapInformation():
    
    JSONPath = "Levels/Levels.JSON"

    with open(JSONPath,'r') as JSONFile:
        LevelDictionary = json.load(JSONFile)
    
    LevelSelection = "Level1"
    
    for Level in LevelDictionary:
        if Level["Name"] == LevelSelection:
           print("Name:", Level["Name"])
           MapName = Level["Name"]
           
           print("Image:", Level["Image"])
           MapImagePath = Level["Image"]
           
           MapHeight = Level["Height"]
           
           MapWidth = Level["Width"]
        
        return MapImagePath, MapHeight, MapWidth

class map(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.background = pygame.Surface((1920,1080))
        self.background.fill((0,0,0))
    
    def render(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.image,(0,0))
