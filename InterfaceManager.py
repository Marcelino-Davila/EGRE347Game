import pygame
import sys

White = (255, 255, 255)  

        


class MenuState:
    def __init__(self, width, height, screen):

        self.width = width
        self.height = height
        self.Screen = screen
        self.Level = "0"
        self.FPS = 240

        self.Font = pygame.font.Font('MenuFont.ttf',120)
        self.SubFont = pygame.font.Font('MenuFont.ttf',75)
        self.SubSubFont = pygame.font.Font('MenuFont.ttf',50)
        
        self.StartText = self.Font.render('Start', True, White)
        self.StartButton = pygame.Rect(0,(height - (height - 0)), 380, 150)

        self.SettingsText = self.SubFont.render('Settings', True, White)
        self.SettingsButton = pygame.Rect(0,(height - (height - 250)), 315, 77)

        self.FPSText = self.SubFont.render('FPS', True, White)
        self.FPSUnderline = self.SubFont.render('___', True, White)

        self.QuitText = self.SubFont.render('Quit', True, White)
        self.QuitButton = pygame.Rect(0,(height - (height - 550)), 170, 77)

        self.OverlayRectangle = pygame.Rect(0,0,width, height)

        self.MenuOverlay = pygame.Surface((width,height),pygame.SRCALPHA)

        




    def ScreenOverlay(self, width, height):
        Alpha = 10
        TitleText = self.Font.render('Menu', True, White)

        #MenuOverlay = pygame.Surface((width,height),pygame.SRCALPHA)
        self.MenuOverlay.fill((0,0,0))

        pygame.draw.rect(self.MenuOverlay, (52,52,52), self.OverlayRectangle)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), self.SettingsButton)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), self.QuitButton)

        self.MenuOverlay.set_alpha(Alpha)

        while True:

            self.Screen.blit(self.MenuOverlay, (0,0))
            self.Screen.blit(TitleText, (0,(height - (height - 10))))
            self.Screen.blit(self.SettingsText, (0, (height - (height - 250))))
            self.Screen.blit(self.QuitText, (0, (height - (height - 550))))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    MousePosition = pygame.mouse.get_pos()

                    if self.SettingsButton.collidepoint(MousePosition):
                        print("Settings Button Clicked")
                        self.SettingsSubMenu(height)
                
                    elif self.QuitButton.collidepoint(MousePosition):
                        print("Quit Button Clicked")
                        pygame.quit()
                        sys.exit()


                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return self.FPS
            
                

    def MainMenu(self, width, height):

        
        StartScreenImage = pygame.image.load('Levels/Images/StartScreen.jpg')
        pygame.draw.rect(self.MenuOverlay, (0,0,0), self.StartButton)

        LevelsText = self.SubFont.render('Levels', True, White)
        LevelsButton = pygame.Rect(0, (height - (height - 400)), 250, 90)

        pygame.draw.rect(self.MenuOverlay, (52,52,52), LevelsButton)

        pygame.draw.rect(self.MenuOverlay, (52,52,52), self.QuitButton)

        while True:
            self.Screen.blit(self.MenuOverlay, (0,0))
            self.Screen.blit(StartScreenImage, (0,0))
            self.Screen.blit(self.StartText, (0,(height - (height - 10))))
            self.Screen.blit(self.SettingsText, (0, (height - (height - 250))))
            self.Screen.blit(LevelsText, (0, (height - (height - 400))))
            self.Screen.blit(self.QuitText, (0, (height - (height - 550))))
            

            pygame.display.update()

            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    MousePosition = pygame.mouse.get_pos()
                    if self.StartButton.collidepoint(MousePosition):
                        return self.Level, self.FPS

                    elif self.SettingsButton.collidepoint(MousePosition):
                        print("Settings Button Clicked")
                        
                        self.SettingsSubMenu(height)

                    elif LevelsButton.collidepoint(MousePosition):
                        print("Levels Button Clicked")
                        self.LevelsSubMenu(height)

                
                    elif self.QuitButton.collidepoint(MousePosition):
                        print("Quit Button Clicked")
                        pygame.quit()
                        sys.exit()
                #print("Main Menu Level Selection:")
                #print(self.SelectedLevel)
                
            
        
        




    def SettingsSubMenu(self, height):
        FPS30Text = self.SubSubFont.render('30', True, White)
        FPS30Button = pygame.Rect(600, (height - (height - 400)), 55, 50)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), FPS30Button)

        FPS60Text = self.SubSubFont.render('60', True, White)
        FPS60Button = pygame.Rect(600, (height - (height - 500)), 55, 50)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), FPS60Button)

        FPS120Text = self.SubSubFont.render('120', True, White)
        FPS120Button = pygame.Rect(600, (height - (height - 600)), 80, 50)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), FPS120Button)

        FPS240Text = self.SubSubFont.render('240', True, White)
        FPS240Button = pygame.Rect(600, (height - (height - 700)), 90, 50)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), FPS240Button)

        Escape = False
        while Escape is False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Escape = True
                else:

                    self.Screen.blit(self.FPSText, (600, (height - (height - 250))))
                    self.Screen.blit(self.FPSUnderline, (600, (height - (height - 280))))
                    self.Screen.blit(FPS30Text, (600, (height - (height - 400))))
                    self.Screen.blit(FPS60Text, (600, (height - (height - 500))))
                    self.Screen.blit(FPS120Text, (600, (height - (height - 600))))
                    self.Screen.blit(FPS240Text, (600, (height - (height - 700))))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        MousePosition = pygame.mouse.get_pos()

                        if FPS30Button.collidepoint(MousePosition):
                            print("30 FPS Selected")
                            self.FPS = 30
                        elif FPS60Button.collidepoint(MousePosition):
                            print("60 FPS Selected")
                            self.FPS = 60
                        elif FPS120Button.collidepoint(MousePosition):
                            print("120 FPS Selected")
                            self.FPS = 120
                        elif FPS240Button.collidepoint(MousePosition):
                            print("240 FPS Selected")
                            self.FPS = 240
                        elif self.QuitButton.collidepoint(MousePosition):
                            print("Quit Button Clicked")
                            pygame.quit()
                            sys.exit()

                    Escape = False

            pygame.display.update()

    def LevelsSubMenu(self, height):

        LabText = self.SubSubFont.render('Lab', True, White)
        LabButton = pygame.Rect(300, (height - (height - 400)), 80, 50)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), LabButton)

        JungleText = self.SubSubFont.render('Jungle', True, White)
        JungleButton = pygame.Rect(300, (height - (height - 500)), 180, 50)
        pygame.draw.rect(self.MenuOverlay, (52,52,52), JungleButton)

        Escape = False
        while Escape is False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Escape = True
                else:
                    self.Screen.blit(LabText, (300, (height - (height - 400))))
                    self.Screen.blit(JungleText, (300, (height - (height - 500))))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        MousePosition = pygame.mouse.get_pos()

                        if LabButton.collidepoint(MousePosition):
                            print("Lab Selected")
                            self.Level = "Level1"
                        elif JungleButton.collidepoint(MousePosition):
                            print("Jungle Selected")
                            self.Level = "Level2"
                        elif self.QuitButton.collidepoint(MousePosition):
                            print("Quit Button Clicked")
                            pygame.quit()
                            sys.exit()

                    Escape = False

            pygame.display.update()



        
