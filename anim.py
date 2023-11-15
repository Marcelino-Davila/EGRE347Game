import pygame

class Animator:
    def __init__(self,color,x,y,width,height):
        self.color = color
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (250,250)

    def rotate(self,angle):
        img1 = pygame.transform.rotate(self.image,angle)
        rect1 = img1.get_rect()
        rect1.center = self.rect.center
        return img1,rect1