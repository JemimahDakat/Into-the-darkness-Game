import pygame, sys
vec = pygame.math.Vector2

class CameraFocus:
    def __init__(self, Navi):
        self.player = Navi 
        self.offsetvalue = vec(0,0)
        self.offsetvalue_float = vec(0,0)
        self.height , self.width = 78, 338
        self.constant= vec(-self.width / 2 + Navi.rect.w / 2, -self.Navi.ground_y +20)

    def setscroll(self, method):
        self.scroll = method 

