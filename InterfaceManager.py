import pygame

height = 720
width = 1240
White = (255, 255, 255)   

class MenuState:
    def __init__(self):
        self.Font = pygame.font.Font('MenuFont.ttf',120)
        self.SubFont = pygame.font.Font('MenuFont.ttf',75)

        self.SettingsText = self.SubFont.render('Settings', True, White)
        self.SaveText = self.SubFont.render('Save', True, White)
        self.QuitText = self.SubFont.render('Quit', True, White)
        self.Screen = pygame.display.set_mode((width,height))

    def ScreenOverlay(self):

        TitleText = self.Font.render('Menu', True, White)

        MenuOverlay = pygame.Surface((width,height),pygame.SRCALPHA)
        Alpha = 128

        MenuOverlay.fill((0, 0, 0, Alpha))


        while True:

            self.Screen.blit(MenuOverlay, (0,0))
            self.Screen.blit(TitleText, (0,(height - (height - 10))))
            self.Screen.blit(self.SettingsText, (0, (height - (height - 250))))
            self.Screen.blit(self.SaveText, (0, (height - (height - 400))))
            self.Screen.blit(self.QuitText, (0, (height - (height - 550))))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
    #def MainMenu():

   
        