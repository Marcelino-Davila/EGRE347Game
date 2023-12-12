import pygame
import math

class lazerImage():
    def __init__(self):
        self.image = pygame.Surface((9000,3))
        self.image.fill((255,10,10))
        self.image.set_colorkey((0,0,0))
    def render(self,screen,centerx,centery,rect):
        x,y = pygame.mouse.get_pos()
        angle = math.atan2(x-centerx,y-centery)*180/3.14
        picture = pygame.transform.rotate(self.image,angle)
        screen.blit(picture,rect)

baseLazer = lazerImage()

class lazerBeams(pygame.sprite.Sprite):
    def __init__(self,parent):
        super().__init__()
        self.ability = "lazer"
        self.parent = parent
        self.image = baseLazer
        self.rect = pygame.Rect(
            self.parent.rect.x,self.parent.rect.y,9000,3
        )
        self.delete = False
        self.explode = True

    def render(self,screen):
        self.image.render(screen,self.rect.centerx,self.rect.centery,self.rect)

    def update(self):
        self.rect.x = self.parent.rect.x
        self.rect.y = self.parent.rect.y
        if not self.parent.ability:
            self.delete = True
    