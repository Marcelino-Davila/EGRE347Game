import pygame

import actor

width = 1240
height = 720

green = (0,255,0)
black = (0,0,0)

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN
        ])

        self.player = actor.Player(green,250,250,150,50)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill("black")
            self.player.render(self.screen)
            self.player.processInput(pygame.key.get_pressed())
            self.player.update()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game(width, height)
    game.loop()