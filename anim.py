import pygame

class Animator:
    def __init__(self,image,x,y,scale=0):
        self.surf = pygame.transform.scale_by(image,scale)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def rotate(self,angle):
        img = pygame.transform.rotate(self.surf,angle)
        return img