#python game
import pygame, sys
from pygame import mixer 
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 600

# naming the game window and fonts
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Into the Darkness')
font = pygame.font.Font("ka1.ttf", 60)
smallerfont= pygame.font.Font("ka1.ttf", 30)


#where the background image will be loaded
bg_img = pygame.image.load('playing_background.gif')
overlap_img = pygame.image.load('playing_background.gif')
path_img = pygame.image.load('play_path.png')
#where characters images will be stored 
navi_walkr = [pygame.image.load('navi_walk1.png'),pygame.image.load('navi_walk2.png'), pygame.image.load('navi_stand.png')]
navi_walkl = [pygame.image.load('navi_walkleft.png'), pygame.image.load('navi_walkleft2.png'), pygame.image.load('navi_walkleft3.png')]
navi4_img = pygame.image.load('navi_still.png')
navi4_img = pygame.transform.scale(navi4_img, (140, 175))
#where the fish collected image is stored
fish_img = pygame.image.load('fish.png')



class Navi(pygame.sprite.Sprite):
    def __init__(self, image_path, image_path_right, image_path_left, x, y):
        super().__init__()
        self.images = [pygame.image.load(image_path), pygame.image.load(image_path_right), pygame.image.load(image_path_left)]
        self.image = self.images[0]  # original image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.move_right = False
        self.move_left = False
        self.jump = False
        self.jump_height = 20
        self.y_direction = 1
        self.y_velocity = self.jump_height
    def update(self):
        if self.move_right:
            self.image = self.images[1]
            if pygame.key.get_pressed()[pygame.K_s]:
                self.rect.x += self.speed * 2
            else:
                self.rect.x += self.speed
        elif self.move_left:
            self.image = self.images[2]
            if pygame.key.get_pressed()[pygame.K_s]:
                self.rect.x -= self.speed * 2
            else:
                self.rect.x -= self.speed
        else:
            self.image = self.images[0]
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.jump = True 
        if self.jump: 
            self.rect.y -= self.y_velocity 
            self.y_velocity -= self.y_direction
            jumpSound = mixer.Sound("jump_sound.wav")
            jumpSound.play()
            jumpSound.set_volume(0.3)
            if self.y_velocity < -self.jump_height:
                self.jump = False
                self.y_velocity = self.jump_height
            

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move_right = True
            elif event.key == pygame.K_LEFT:
                self.move_left = True
            elif event.key == pygame.K_UP:
                self.jump = True 
        
                if not self.jump:
                    self.fall = True
                    self.jump = False 
                    self.max_height = self.rect.y - self.jump_height
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.move_right = False
            elif event.key ==pygame.K_UP:
                self.fall = True
            elif event.key == pygame.K_LEFT:
                self.move_left = False


navi = Navi("navi_still.png","navi_walk1.png", "navi_walkleft.png", x =78, y= 338)
navi_group = pygame.sprite.Group()
navi_group.add(navi)