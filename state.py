import pygame.locals as keys

class PlayerState:
    def __init__(self, parent):
        self.parent = parent

    def processInput(self, pressed):
        pass
    
    def update(self):
        pass
    
class StandingState(PlayerState):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent.kinem.vel_x = 0
        self.parent.kinem.vel_y = 0
        print("standing")

    def processInput(self, pressed):
        if pressed[keys.K_a]:
            return moving(self.parent,x=-10)
        if pressed[keys.K_d]:
            return moving(self.parent,x=10)
        if pressed[keys.K_w]:
            return moving(self.parent,y=-10)
        if pressed[keys.K_s]:
            return moving(self.parent,y=10)

class moving(PlayerState):
    def __init__(self, parent,x=0,y=0):
        super().__init__(parent)
        self.parent.kinem.vel_x = x
        self.parent.kinem.vel_y = y
        print("moving")

    def processInput(self, pressed):
        if pressed[keys.K_a]:
            self.parent.kinem.vel_x = -10
        if pressed[keys.K_d]:
            self.parent.kinem.vel_x = 10
        if pressed[keys.K_w]:
            self.parent.kinem.vel_y = -10
        if pressed[keys.K_s]:
            self.parent.kinem.vel_y = 10
        else:
            return StandingState(self.parent)