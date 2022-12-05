import pygame
import Button
import Tron
from pygame import mixer

pygame.init()
mixer.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT) )

#sets caption
pygame.display.set_caption("Main Menu")

#loads background image
bg = pygame.image.load("background-image.jpg")

start = False

#FONTS
font = pygame.font.SysFont("arialblack",50)
button_font = pygame.font.SysFont("arialblack",25)
speed_font = pygame.font.SysFont("arialblack",18)

#COLORS
txt_color = (255,191,0)

#load images
button_frame = pygame.image.load("logo.jpg")
start_button_frame = pygame.image.load("button-image.jpg")

#making main tron logo
logo = Button.Button(115,210,button_frame,1)

#making first start button
start_button = Button.Button(45,315,start_button_frame,1)
slow_button = Button.Button(200,322,start_button_frame,0.7)
fast_button = Button.Button(290,322,start_button_frame,0.7)

#load and play music
mixer.music.load('background-music.wav')
mixer.music.play()

#draw text function
def draw_text(text,font,txt_color,x,y):
    img = font.render(text,True,txt_color)
    screen.blit(img,(x,y))

speed = 0
run = True
while run:
    screen.blit(bg,(0,0))

    #draws background
    logo.draw(screen)

    draw_text("TRON",font,txt_color,124,212)

    #main if statement that plays game if player clicks on button
    if start_button.draw(screen):
        x = Tron.game(400,400, 200)
        x.start_play()
    if fast_button.draw(screen):
        x = Tron.game(400,400, 100)
        x.start_play()
    if slow_button.draw(screen):
        x = Tron.game(400,400, 300)
        x.start_play()

    #draw text on screenS
    draw_text("START",button_font,txt_color,55,325)
    draw_text("SLOW",speed_font,txt_color,213,331)
    draw_text("FAST",speed_font,txt_color,305,331)

    #getting mouse position and quitting if inputed
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            start = True
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()



# WHEN WE LOAD IN THIS MODULE TO TRON, WE MUST ALSO LOAD IN THE IMAGES; IMG NAME = pygame.img.load("PATHWAY TO IMAGE HERE")