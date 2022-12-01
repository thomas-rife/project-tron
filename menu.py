import pygame
import Button

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT) )

pygame.display.set_caption("Main Menu")

bg = pygame.image.load("Documents/CMSI1010/project-tron/background-image.jpg")

start = False

#FONTS
font = pygame.font.SysFont("arialblack",50)
button_font = pygame.font.SysFont("arialblack",25)
#COLORS
txt_color = (255,191,0)

######## BUTTON CLASS ############

#load images
button_frame = pygame.image.load("Documents/CMSI1010/project-tron/logo.jpg")
start_button_frame = pygame.image.load("Documents/CMSI1010/project-tron/button-image.jpg")



#making main tron logo
logo = Button.Button(115,210,button_frame,1)

#making first start button
start_button = Button.Button(45,315,start_button_frame,1)
other_button = Button.Button(255,315,start_button_frame,1)

#######################################################

def draw_text(text,font,txt_color,x,y):
    img = font.render(text,True,txt_color)
    screen.blit(img,(x,y))

run = True
while run:
    screen.blit(bg,(0,0))
    logo.draw(screen)

    draw_text("TRON",font,txt_color,124,212)


    if start_button.draw(screen):
        print("start")
    if other_button.draw(screen):
        print("Speed")


    draw_text("START",button_font,txt_color,55,325)
    draw_text("SPEED",button_font,txt_color,265,325)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            start = True
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()



# WHEN WE LOAD IN THIS MODULE TO PYGAME, WE MUST ALSO LOAD IN THE IMAGES; IMG NAME = pygame.img.load("PATHWAY TO IMAGE HERE")