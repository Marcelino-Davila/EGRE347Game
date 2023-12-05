import pygame
from entity_manager import entityManager
import PlayerClass
import enemies
import actor
from LevelManager import MapInformation

MapName, MapImagePath, MapHeight, MapWidth = MapInformation()

width = MapWidth
height = MapHeight
FPS = 120

green = (0,255,0)
black = (0,0,0)

class Game:
    def __init__(self, width, height, MapImagePath):
        pygame.init()
        self.selectedClass=0 #selecting level and class from main menu then run entitnymanager.loadlevel()
        self.selectedLevel=0 
        self.entityManager = entityManager()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN
        ])
        self.player = PlayerClass.soldier(750,750)
        self.wall = actor.coliders(100,100,10,200)
        self.enemy = enemies.enemies(200,200,self.player)
        self.entityManager.addEntity(self.player,"Player")
        self.entityManager.addEntity(self.enemy,"Enemy")
        self.entityManager.addEntity(self.wall,"Walls")
        self.MapImage = pygame.image.load(MapImagePath)
        
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            self.screen.blit(self.MapImage, (0, 0))
            self.entityManager.renderAll(self.screen,False)#need to know if paused
            self.entityManager.updateAll(False)
            self.entityManager.checkCollisions()
            self.player.processInput(pygame.key.get_pressed())
            bullet = self.player.processMouse(pygame.mouse.get_pressed())
            if bullet:
                self.entityManager.addEntity(bullet,"AllyBullets")
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game(width, height, MapImagePath)
    game.loop()