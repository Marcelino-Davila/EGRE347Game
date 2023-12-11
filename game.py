import pygame
import pygame.locals as keys
from entity_manager import entityManager
import PlayerClass
import enemies
import actor
from LevelManager import MapInformation
import math
import LevelManager
import enemiesList
from InterfaceManager import MenuState

MapName, MapImagePath, MapHeight, MapWidth = MapInformation()

width = MapWidth
height = MapHeight
FPS = 240

green = (0,255,0)
black = (0,0,0)

class Game:
    def __init__(self, width, height, MapImagePath):
        pygame.init()
        
        self.esc = False
        self.width = width
        self.height = height

        self.selectedClass=0 #selecting level and class from main menu then run entitnymanager.loadlevel()
        self.selectedLevel=0 
        self.entityManager = entityManager()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN
        ])
        self.player = PlayerClass.Gojira(750,750)
        self.player = PlayerClass.soldier(750,750)
        self.wall = actor.coliders(100,100,10,200)
        self.enemy = enemies.enemies(200,200,self.player)
        #self.enemy = enemiesList.swat(200,200,self.player)
        #self.enemy = enemiesList.police(200,200,self.player)
        self.entityManager.addEntity(self.player,"Player")
        self.entityManager.addEntity(self.enemy,"Enemy")
        self.entityManager.addEntity(self.wall,"Walls")
        self.MapImage = pygame.image.load(MapImagePath)
        self.Menu_State = MenuState(width, height, self.screen, FPS)
        

    def loop(self):
        picture_width = self.MapImage.get_width() #gets what the width of the background is
        movePic = 0
        imagecount = math.ceil(width / picture_width) + 1 #finds the number images to 

        self.Menu_State.MainMenu(width, height, FPS)
        
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

            if pygame.key.get_pressed()[pygame.K_ESCAPE] and not self.esc:
                self.esc = True
                self.Menu_State.ScreenOverlay(width, height, FPS)
               #NewFPS = MenuState.ScreenOverlay(FPS)
                #FPS = NewFPS
            if not pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.esc = False
            
            self.clock.tick(FPS)

            for i in range(0, imagecount): #takes the image and places it on the right continuously
                self.screen.blit(self.MapImage, (i * picture_width + movePic, 0))

            movePic -= 5
            
            if abs(movePic) > picture_width: #places the image back
                movePic = 0


if __name__ == "__main__":
    game = Game(width, height, MapImagePath)
    game.loop()