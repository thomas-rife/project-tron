import pygame

class Button():
    def __init__(self,x,y,image,scale):
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image,(int(w*scale),int(h*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,surface):
        #get mouse position
        mouse_position = pygame.mouse.get_pos()
        boolean = False

        #check mouseover and click
        if self.rect.collidepoint(mouse_position):
            #next if statement checks if mouse 1 (left click or [0] right click is [2] and middle is [0]) gets pressed
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                boolean = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #drawing image/button
        surface.blit(self.image,(self.rect.x,self.rect.y))

        return boolean