import pygame.locals as keys
import math

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
        self.parent.wallCollide = True
        self.speed = speed
        self.w = True
        self.a = True
        self.s = True
        self.d = True
        self.e = True

    def processInput(self, pressed):
        xspeed = 0
        yspeed = 0
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
        if pressed[keys.K_e] and self.e == True:
            self.parent.ability = True
            self.e = False
        else:
            self.parent.ability = False
            self.e = True
        if self.parent.jump:
            return rocketJump(self.parent,self.speed)
        self.parent.kinem.vel_x = xspeed
        self.parent.kinem.vel_y = yspeed

    def update(self):
        if self.parent.rocketJump == True:
            return rocketJump(self.parent,self.speed)


class rocketJump(PlayerState):
    def __init__(self,parent,speed):
        super().__init__(parent)
        self.parent.WallCollide = False
        self.count = 0
        self.speed = speed
        x,y = self.parent.grenadeCoord
        x+=30
        y+=30
        self.angle = math.atan2(x-self.parent.rect.x+25,y-self.parent.rect.y+25)
        self.parent.kinem.vel_y = 2*math.cos(self.angle)
        self.parent.kinem.vel_x = -2*math.sin(self.angle)
    
    def update(self):
        self.count+=1
        if self.count > 100:
            self.parent.jump = False

        if not self.parent.jump:
            return moving(self.parent,self.speed)
