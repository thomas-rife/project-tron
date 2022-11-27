"""
The tron game.
Brian, Thomas, Robert
"""
import sys, pygame
pygame.init()

class snake:
    pass

class game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def create_screen(self):
        screen = pygame.display.set_mode([self.height, self.width])
        
    def add_background(self, image):
        background = pygame.image.load(image)
        #back_rect = background.get_rect()
    
    def start(self):
        'This keeps the screen displaying until the screen windown is closed'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.create_screen()
            self.add_background()
            

class player:
    pass

x = game(400,400)
x.start()