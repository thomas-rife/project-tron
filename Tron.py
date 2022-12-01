"""
The tron game.
Brian, Thomas, Robert
"""
import sys, pygame
pygame.init()

class snake:
    def __init__(self, screen, color, left_player, moves):
        self.screen = screen
        self.color = color
        self.left_player = left_player
        self.current_x = 0
        self.current_y = 0
        self.moves = moves

    def get_size(self):
        size = pygame.display.get_surface().get_size()
        return size

    #draws the start square of the snake starting at the correct position depending on if its the right or left snake
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
        self.moves.append((self.current_x, self.current_y))
    
    #draws a square in the given direction and checks to see if the snake's move is illegal to which it will return true.
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
        if (self.current_x, self.current_y) in self.moves or self.current_x <0 or self.current_x > (x - x/20) or self.current_y < 0 or self.current_y > (y - y/20):
            return True
        self.moves.append((self.current_x, self.current_y))
        

class game:

    def __init__(self, height, width, difficulty):
        self.height = height
        self.width = width   
        self.difficulty = difficulty
        self.moves = []

    #creates the screen for the snakes
    def create_screen(self):
        screen = pygame.display.set_mode([self.height, self.width])
        pygame.display.set_caption('Tron') 
        screen.fill((255,255,255))
        return screen
    
    #draws the starting grid with 20 by 20 squares    
    def draw_grid(self, screen):
        x_value = 0
        y_value = 0
        for x in range(20):
            for y in range(20):
                pygame.draw.rect(screen, (0,0,0), [x_value, y_value, self.width/20, self.height/20], 3)
                y_value += self.height/20
            x_value += self.width/20
            y_value = 0
    '''
    def new_screen(self, screen):
        
        
        return (snake1, snake2)
        '''
    #this function initilizes the snakes and the players and starts the game
    def start_play(self):
        for x in range(3):
            screen = self.create_screen()
            self.moves = []
            screen.fill((255,255,255))
            self.draw_grid(screen)
            snake1 = snake(screen, (255, 16, 240), True, self.moves)
            snake1.draw_snake() 
            snake2 = snake(screen, (255,234,0), False, self.moves) 
            snake2.draw_snake()
            pygame.display.update() 
            'This keeps the screen displaying until the screen window is closed'
            player1 = player(0, 'letters',snake1, 'right')
            player2 = player(0, 'arrows', snake2, 'left')
            
            "add a countdown function so its not right away"

            #this is the loop that allows for the snake to look like its moving
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                
                    if event.type == pygame.KEYDOWN:
                        player1.player_input(event)
                        player2.player_input(event)
                if snake1.extend_snake(player1.dir):
                    break
                elif snake2.extend_snake(player2.dir):
                    break
                else:    
                    pygame.display.update()
                    pygame.time.wait(self.difficulty)
            

class player:
    'need to get the users inputs and keep track of their scores'
    def __init__(self, score, keys, snake, dir):
        self.score = score
        self.keys = keys
        self.snake = snake
        self.dir = dir
        
    #this class takes in the event and checks to see if the move is allowed (not in the opposite direction) and returns the direction to move
    def player_input(self, event):
        anti_direct = {'left':'right', 'right':'left', 'up':'down', 'down':'up'}
        if self.keys == 'letters':
            input_letters = {pygame.K_a : 'left', pygame.K_s : 'down',pygame.K_d : 'right',pygame.K_w : 'up'}
            if event.key in input_letters:
                  direct = input_letters[event.key]
                  if direct != anti_direct[self.dir]:
                    self.dir = direct

        elif self.keys == 'arrows':
            input_arrows = {pygame.K_UP: 'up', pygame.K_DOWN: 'down' , pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right'} 
            if event.key in input_arrows:
                direct = input_arrows[event.key]
                if direct != anti_direct[self.dir]:
                    self.dir = direct

        return self.dir