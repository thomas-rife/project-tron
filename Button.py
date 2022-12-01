import pygame


class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,surface):
        #get mouse position
        pos = pygame.mouse.get_pos()
        action = False

        #check mouseover and click
        if self.rect.collidepoint(pos):
            #next if statement checks if mouse 1 (left click or [0] right click is [2] and middle is [0]) gets pressed
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #drawing image/button
        surface.blit(self.image,(self.rect.x,self.rect.y))

        return action