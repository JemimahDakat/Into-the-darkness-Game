import pygame

pygame.init()

window = pygame.display.set_mode((1000,600))

#button class
class Button():
     def __init__(self, x, y, pics, pic2, scale):
        width = pics.get_width()
        height = pics.get_height()
        self.pics = pygame.transform.scale(pics, (int(width * scale), int(height * scale)))
        self.pics = pics 
        self.pic2 = pygame.transform.scale(pics, (int(width * scale), int(height * scale)))
        self.pic2 = pic2
        self.original_pic = pics
        self.rect = self.pics.get_rect()
        self.rect.topleft = (x, y)
position = pygame.mouse.get_pos()



