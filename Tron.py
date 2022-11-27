"""
The tron game.
Brian, Thomas, Robert
"""
import sys, pygame
pygame.init()

class snake:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color

    def draw_snake(self):
        start_x = self.screen.width *2
        start_y = self.screen.height/2
        pygame.draw.rect(self.screen, self.color, [start_x, start_y, self.width/20, self.height/20])
    
    def extend_snake(self, direction):
        pass

class game:

    def __init__(self, height, width):
        self.height = height
        self.width = width   

    def create_screen(self):
        screen = pygame.display.set_mode([self.height, self.width])
        pygame.display.set_caption('Tron') 
        screen.fill((255,255,255))
        return screen
        
    def add_background(self, image):
        background = pygame.image.load(image)
        #back_rect = background.get_rect()

    def draw_grid(self, screen):
        x_value = 0
        y_value = 0
        for x in range(20):
            for y in range(20):
                pygame.draw.rect(screen, (0,0,0), [x_value, y_value, self.width/20, self.height/20], 3)
                y_value += self.height/20
            x_value += self.width/20
            y_value = 0
    
    def start_play(self):

        screen = self.create_screen()
        self.draw_grid(screen)
        pygame.display.update() 

        snake1 = snake(screen, ())   

        'This keeps the screen displaying until the screen window is closed'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            

class player:
    'need to get the users inputs and keep track of their scores'
    pass


x = game(400,400)
x.start_play()