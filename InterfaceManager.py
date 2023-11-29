import pygame

height = 900
width = 900

White = (255, 255, 255)     

class MenuState:
    def ScreenOverlay():
        Font = pygame.font.Font('MenuFont.ttf',120)
        SubFont = pygame.font.Font('MenuFont.ttf',75)
        TitleText = Font.render('Menu', True, White)
        SettingsText = SubFont.render('Settings', True, White)
        SaveText = SubFont.render('Save', True, White)
        QuitText = SubFont.render('Quit', True, White)

        Screen = pygame.display.set_mode((width,height))
        MenuOverlay = pygame.Surface((width,height),pygame.SRCALPHA)
        MenuOverlay.fill((0, 0, 0, 50))
        MenuOverlay.set_alpha(100)

        while True:
            Screen.blit(MenuOverlay, (0,0))
            Screen.blit(TitleText, (0,(height - (height - 10))))
            Screen.blit(SettingsText, (0, (height - (height - 250))))
            Screen.blit(SaveText, (0, (height - (height - 400))))
            Screen.blit(QuitText, (0, (height - (height - 550))))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
   
        