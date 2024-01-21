
import pygame, sys
import time
from pygame import mixer
from pygame.locals import * 
from game import Navi
pygame.init()

mixer.music.load("playing_music.wav.wav")
mixer.music.play(-1)
screen_width = 1000
screen_height = 600

# naming the game window and fonts
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Into the Darkness')
font = pygame.font.Font("ka1.ttf", 60)
smallerfont= pygame.font.Font("ka1.ttf", 30)


#where the background image will be loaded
bg1_img = pygame.image.load('menu_background.png')
text_colour = (0, 0, 0)

#load button pictures
play_img = pygame.image.load('play_button.png').convert_alpha()
play_hover_img = pygame.image.load('playC_button.png').convert_alpha()

score_img = pygame.image.load('score_button.png').convert_alpha()
score_hover_img = pygame.image.load('scoreC_button.png').convert_alpha()

inst_img = pygame.image.load('instr_button.png').convert_alpha()
inst_hover_img = pygame.image.load('instrC_button.png').convert_alpha()

#where the background image will be loaded
bg_img = pygame.image.load('playing_background.gif')
overlap_img = pygame.image.load('playing_background.gif')
path_img = pygame.image.load('play_path.png')

navi_walkr = [pygame.image.load('navi_walk1.png'),pygame.image.load('navi_walk2.png'), pygame.image.load('navi_stand.png')]
navi_walkl = [pygame.image.load('navi_walkleft.png'), pygame.image.load('navi_walkleft2.png'), pygame.image.load('navi_walkleft3.png')]
navi4_img = pygame.image.load('navi_still.png')
navi4_img = pygame.transform.scale(navi4_img, (140, 175))
#where the fish collected image is stored
fish_img = pygame.image.load('fish.png')


def title():
    title = font.render('Into The Darkness', True, text_colour)
    title_rect = title.get_rect(center = screen.get_rect().center)
    titleinst = smallerfont.render('Press space to continue', True, text_colour)
    titleinst_rect = titleinst.get_rect(midbottom = screen.get_rect().midbottom)
    screen.blit(bg1_img, (0, 0))
    screen.blit(title, title_rect)
    screen.blit(titleinst, titleinst_rect)

def main_menu():
    main_menu_text = font.render('Main Menu', True, text_colour)
    main_menu_rect = main_menu_text.get_rect(midtop = screen.get_rect().midtop)
    screen.blit(bg1_img, (0, 0))
    screen.blit(main_menu_text, main_menu_rect)

    play_button.draw()
    play_button.change_image(mouse_pos)

    scoreboard_button.draw()
    scoreboard_button.change_image(mouse_pos)
    

    instructions_button.draw()
    instructions_button.change_image(mouse_pos)

    if play_button_clicked:
        Starterpage()
    if inst_button_clicked:
        inst_page()

def inst_page():
    inst_page_text = font.render('Instructions',True, text_colour)
    inst_page_rect = inst_page_text.get_rect(midtop = screen.get_rect().midtop)
    inst_page1_text = smallerfont.render('There are 6 levels in this game, \n each with a incresaing level of difficulty.\n the aim of the game is to help guide navi \n through the dark caves back to the comfort of his home. \n Help Navi by collecting fish to make his eyesight better! at the end of each sucessful level,\n you can compare your best times with freinds!!! ',True, text_colour)
    inst_page1_rect = inst_page_text.get_rect(center = screen.get_rect().center)
    screen.blit(bg1_img, (0, 0))
    screen.blit(inst_page_text, inst_page_rect)
    screen.blit(inst_page1_text, inst_page1_rect)


def starterlvl():
    background_size = bg_img.get_size()
    background_rect = bg_img.get_rect()
    screen = pygame.display.set_mode(background_size)
    screen.blit(bg_img,background_rect)
    screen.blit(path_img, (-30,400))
    navi_group.draw(screen)


navi = Navi("navi_still.png","navi_walk1.png", "navi_walkleft.png",x=78, y=200)
navi_group = pygame.sprite.Group()
navi_group.add(navi)


 
def Starterpage():
    screen.fill ((255,255,255))
    StarterLevel = font.render('Practice Level!', True, text_colour)
    starter_rect = StarterLevel.get_rect(center = screen.get_rect().center)
    startinst = smallerfont.render('Press enter to continue', True, text_colour)
    startinst_rect = startinst.get_rect(midbottom = screen.get_rect().midbottom)
    
    screen.blit(StarterLevel, starter_rect)
    screen.blit(startinst, startinst_rect)

    if enter_press:
        starterlvl()


#class for buttons
class mainmenubutton():
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
    print(position)

    def check_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
           return True

    def draw(self):
    #displays buttons on screen 
        screen.blit(self.pics, (self.rect.x, self.rect.y))

    def change_image(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
           self.pics = self.pic2
        else: 
            self.pics = self.original_pic

        

#creating class objects 
play_button = mainmenubutton(300,400,play_img, play_hover_img, 0.3)
scoreboard_button = mainmenubutton(215,240,score_img, score_hover_img, 0.3)
instructions_button = mainmenubutton(120,70,inst_img, inst_hover_img, 0.3)

space_pressed = False
enter_press = False
play_button_clicked = False
inst_button_clicked = False
 
#game loop 
game = True
while game:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            sys.exit()

        
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = True
            else:
                 space_pressed = False
    
            if event.key == pygame.K_RETURN:
                enter_press = True
            else:
                enter_press = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.check_input(mouse_pos):
                play_button_clicked = True
            else:
                play_button_clicked = False
            if instructions_button.check_input(mouse_pos):
                inst_button_clicked = True
            else:
                inst_button_clicked = False

    mouse_pos = pygame.mouse.get_pos()
    title()
    if space_pressed:
        main_menu()

    if enter_press:
        starterlvl()

        
#Event handling here
    for event in pygame.event.get():
        navi.handle_event(event)
    navi.update()
    pygame.display.flip()     

    
