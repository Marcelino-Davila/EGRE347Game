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
    def __init__(self, parent,speed):
        super().__init__(parent)
        self.speed = speed
        self.w = True
        self.a = True
        self.s = True
        self.d = True
        self.esc = False

    def processInput(self, pressed):
        xspeed = 0
        yspeed = 0
        if pressed[keys.K_SPACE]:
            self.parent.gun()
        if pressed[keys.K_w] and self.w == True:
            yspeed -=self.speed
            self.w = False
        else:
            yspeed +=self.speed 
            self.w = True
        if pressed[keys.K_a] and self.a == True:
            xspeed -=self.speed
            self.a = False
        else: 
            xspeed +=self.speed
            self.a = True
        if pressed[keys.K_s] and self.s == True:
            yspeed +=self.speed
            self.s = False
        else: 
            yspeed -=self.speed
            self.s = True
        if pressed[keys.K_d] and self.d == True:
            xspeed +=self.speed
            self.d = False
        else: 
            xspeed -=self.speed
            self.d = True
        if pressed[keys.K_ESCAPE] and not self.esc:
            self.esc = True
            MenuState.ScreenOverlay()
        if not pressed[keys.K_ESCAPE]:
            self.esc = False
        self.parent.kinem.vel_x = xspeed
        self.parent.kinem.vel_y = yspeed