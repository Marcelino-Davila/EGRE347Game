import pygame
from entity_manager import entityManager
import PlayerClass
from LevelManager import MapInformation

MapName, MapImagePath, MapHeight, MapWidth = MapInformation()

width = MapWidth
height = MapHeight
FPS = 240

green = (0,255,0)
black = (0,0,0)

class Game:
    def __init__(self, width, height, MapImagePath):
        pygame.init()
        self.entityManager = entityManager()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN
        ])
        self.player = PlayerClass.Gojira(250,250)
        self.entityManager.addEntity(self.player,"Player")
        self.MapImage = pygame.image.load(MapImagePath)
        
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            self.screen.blit(self.MapImage, (0, 0))
            
            self.entityManager.renderAll(self.screen)
            self.entityManager.updateAll()
            self.player.processInput(pygame.key.get_pressed())
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game(width, height, MapImagePath)
    game.loop()