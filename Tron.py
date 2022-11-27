"""
The tron game.
Brian, Thomas, Robert
"""
import sys, pygame
pygame.init()

class snake:
    def __init__(self, screen, color, left_player):
        self.screen = screen
        self.color = color
        self.left_player = left_player
        self.current_x = 0
        self.current_y = 0

    def get_size(self):
        size = pygame.display.get_surface().get_size()
        return size

    def draw_snake(self):
        x,y = self.get_size()
        if self.left_player:
            start_x = x/20 *2
        else:
            start_x = x - (x/20 *3)
        self.current_x = start_x
        start_y = y/2
        self.current_y = start_y
        pygame.draw.rect(self.screen, self.color, [start_x, start_y, x/20, y/20])
    
    def extend_snake(self, direction):
        'direction is in relation to the screen, not in regard to the snake'
        x,y = self.get_size()
        directions = {'up': -(y/20), 'down': (y/20), 'left': -(x/20), 'right': x/20}
        if direction == 'left' or direction == 'right':
            pygame.draw.rect(self.screen, self.color, [self.current_x + directions[direction], self.current_y, x/20, y/20])
            self.current_x += directions[direction]
        else:
            pygame.draw.rect(self.screen, self.color, [self.current_x, self.current_y + directions[direction], x/20, y/20])
            self.current_y += directions[direction]


class game:

    def __init__(self, height, width, difficulty):
        self.height = height
        self.width = width   
        self.difficulty = difficulty

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

        snake1 = snake(screen, (255, 0, 0), True)
        snake1.draw_snake() 
        snake2 = snake(screen, (0,0,255), False) 
        snake2.draw_snake()
        pygame.display.update() 

        'This keeps the screen displaying until the screen window is closed'
        player1 = player(0, 'letters',snake1, 'right')
        player2 = player(0, 'arrows', snake2, 'left')
        while True:
            direction = player1.dir
            direction2 = player2.dir
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                
                if event.type == pygame.KEYDOWN:
                #and (event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    direction = player1.player_input(event)
                    direction2 = (player2.player_input(event))

            snake1.extend_snake(direction)
            snake2.extend_snake(direction2)
            pygame.display.update()
            pygame.time.wait(self.difficulty)
            
            

class player:
    'need to get the users inputs and keep track of their scores'
    def __init__(self, score, keys, snake, dir):
        self.score = score
        self.keys = keys
        self.snake = snake
        self.dir = dir
        

    def player_input(self, event):
        if self.keys == 'letters':
            input_letters = {pygame.K_a : 'left', pygame.K_s : 'down',pygame.K_d : 'right',pygame.K_w : 'up'}
            if event.key in input_letters:
                self.dir = input_letters[event.key]

        elif self.keys == 'arrows':
            input_arrows = {pygame.K_UP: 'up', pygame.K_DOWN: 'down' , pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right'} 
            if event.key in input_arrows:
                self.dir = input_arrows[event.key]

        return self.dir




x = game(400,400, 200)
x.start_play()