import pygame.locals as keys
from InterfaceManager import MenuState

class PlayerState:
    def __init__(self, parent):
        self.parent = parent

    def processInput(self, pressed):
        pass
    
    def update(self):
        pass

class moving(PlayerState):
    def __init__(self, parent,x=0,y=0):
        super().__init__(parent)
        self.parent.kinem.vel_x = x
        self.parent.kinem.vel_y = y
        self.w = True
        self.a = True
        self.s = True
        self.d = True

    def processInput(self, pressed):
        xspeed = 0
        yspeed = 0
        if pressed[keys.K_SPACE]:
            self.parent.gun()
        if pressed[keys.K_w] and self.w == True:
            yspeed -=5
            self.w = False
        else:
            yspeed +=5 
            self.w = True
        if pressed[keys.K_a] and self.a == True:
            xspeed -=5
            self.a = False
        else: 
            xspeed +=5
            self.a = True
        if pressed[keys.K_s] and self.s == True:
            yspeed +=5
            self.s = False
        else: 
            yspeed -=5
            self.s = True
        if pressed[keys.K_d] and self.d == True:
            xspeed +=5
            self.d = False
        else: 
            xspeed -=5
            self.d = True
        self.parent.kinem.vel_x = xspeed
        self.parent.kinem.vel_y = yspeed