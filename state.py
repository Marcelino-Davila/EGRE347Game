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
        self.esc = False

    def processInput(self, pressed):
        xspeed = 0
        yspeed = 0
        if pressed[keys.K_SPACE]:
            self.parent.gun()
        if pressed[keys.K_w] and self.w == True:
            yspeed -=10
            self.w = False
        else:
            yspeed +=10 
            self.w = True
        if pressed[keys.K_a] and self.a == True:
            xspeed -=10
            self.a = False
        else: 
            xspeed +=10
            self.a = True
        if pressed[keys.K_s] and self.s == True:
            yspeed +=10
            self.s = False
        else: 
            yspeed -=10
            self.s = True
        if pressed[keys.K_d] and self.d == True:
            xspeed +=10
            self.d = False
        else: 
            xspeed -=10
            self.d = True
        if pressed[keys.K_ESCAPE] and not self.esc:
            self.esc = True
            MenuState.ScreenOverlay()
        if not pressed[keys.K_ESCAPE]:
            self.esc = False

        self.parent.kinem.vel_x = xspeed
        self.parent.kinem.vel_y = yspeed
        
