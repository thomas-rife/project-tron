"""
The tron game.
Brian, Thomas, Robert
"""
import sys, pygame
pygame.init()
import time
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

    #draws the start square of the snake starting at the correct position depending on if its the right or left snake
    def draw_snake(self, moves):
        x,y = self.get_size()
        if self.left_player:
            start_x = x/20 *2
        else:
            start_x = x - (x/20 *3)
        self.current_x = start_x
        start_y = y/2
        self.current_y = start_y
        pygame.draw.rect(self.screen, self.color, [start_x, start_y, x/20, y/20])
        moves.append((self.current_x, self.current_y))
    
    #draws a square in the given direction and checks to see if the snake's move is illegal to which it will return true.
    def extend_snake(self, direction, moves):
        'direction is in relation to the screen, not in regard to the snake'
        x,y = self.get_size()
        directions = {'up': -(y/20), 'down': (y/20), 'left': -(x/20), 'right': x/20}
        if direction == 'left' or direction == 'right':
            pygame.draw.rect(self.screen, self.color, [self.current_x + directions[direction], self.current_y, x/20, y/20])
            self.current_x += directions[direction]
        else:
            pygame.draw.rect(self.screen, self.color, [self.current_x, self.current_y + directions[direction], x/20, y/20])
            self.current_y += directions[direction]
        if (self.current_x, self.current_y) in moves or self.current_x <0 or self.current_x > (x - x/20) or self.current_y < 0 or self.current_y > (y - y/20):
            return True
        moves.append((self.current_x, self.current_y))
        

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
    
    #draws the starting grid with 20 by 20 squares - depending on the call to the function    
    def draw_grid(self, screen):
        x_value = 0
        y_value = 0
        for x in range(20):
            for y in range(20):
                pygame.draw.rect(screen, (0,0,0), [x_value, y_value, self.width/20, self.height/20], 3)
                y_value += self.height/20
            x_value += self.width/20
            y_value = 0

    #this starts a new round of play, it fills the screen, draws new snakes and resets the directions
    def new_round(self, snake1, snake2, screen, player1, player2):
        self.moves = []
                    
        screen.fill((255,255,255))
        self.draw_grid(screen)
        player1.dir = 'right'
        player2.dir = 'left'
        snake1.draw_snake(self.moves) 
        snake2.draw_snake(self.moves)
        # self.countdown(screen)
        pygame.display.update()

    #this function draws the winner onto the screen using the winners sides color
    def winner(self, screen, winner, color):
        font = pygame.font.SysFont("arialblack",75)
        img = font.render(winner + ' WINS!',True, color)
        screen.blit(img,(15, 125))

    #this function starts a countdown from 3 at the start of the game
    #displays this countdown before disappearing on the screen
    #draws the countdown on the screen with the color chosen, but the color can be changed in the code to whatever the user wants/prefers
    def countdown(self, screen):
       for x in range(3, 0, -1):
        screen.fill((255,255,255))
        self.draw_grid(screen)
        font = pygame.font.SysFont("arialblack",75)
        img = font.render(str(int(x)), True, 'Purple')
        screen.blit(img,(175, 125))
        pygame.time.delay(1000)
        pygame.display.update()
       screen.fill((255,255,255))
       self.draw_grid(screen)
        
    
    
    #this function initilizes the snakes and the players and starts the game
    def start_play(self):
        
        #for x in range(3):
            screen = self.create_screen()
            snake1 = snake(screen, (255, 16, 240), True)
            snake2 = snake(screen, (255,234,0), False)
            player1 = player('letters',snake1, 'right')
            player2 = player('arrows', snake2, 'left')
            
            self.countdown(screen)
            pygame.time.delay(1000)
            self.new_round(snake1, snake2, screen, player1, player2)
            

            

            #This keeps the screen displaying until the screen window is closed
            #this is the loop that allows for the snake to look like its moving
            while player1.score < 3 and player2.score < 3:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                
                    if event.type == pygame.KEYDOWN:
                        player1.player_input(event)
                        player2.player_input(event)
                pygame.display.update()
                if snake1.extend_snake(player1.dir, self.moves):
                    player1.add_point()
                    self.new_round(snake1, snake2, screen, player1, player2)
                    pygame.time.delay(500)
            #each if and elif statement above and below has a time.delay function that is what causes the pause in between rounds to allow the user to get set up for the next game
                elif snake2.extend_snake(player2.dir, self.moves):
                    player2.add_point()  
                    self.new_round(snake1, snake2, screen, player1, player2)
                    pygame.time.delay(500)
                else:    
                    pygame.display.update()
                    pygame.time.wait(self.difficulty)
                player2.update(screen, (255,16,240), (20, 20))
                player1.update(screen, (255, 234, 0), (350, 20))
            # the if and elif statement below call for the winner screen depending on which player got to 3 points first
            if player1.score == 3:
                self.winner(screen, 'P2', (255, 234, 0))
            elif player2.score == 3:
                self.winner(screen, 'P1', (255,16,240))
            pygame.display.update()
            pygame.time.wait(2500)
                
            

class player:
    'need to get the users inputs and keep track of their scores'
    def __init__(self, keys, snake, dir):
        self.score = 0
        self.keys = keys
        self.snake = snake
        self.dir = dir
        
    #this class takes in the event and checks to see if the move is allowed (not in the opposite direction) and returns the direction to be passed to the extend snake function
    #shows what keys are used for the directions up, down, right, left for both player 1 and 2
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
    #this function adds points to the score seen on both the top left and right of the screen when starting the game
    def add_point(self):
        self.score += 1
    #this function is used to draw the score onto the screens, with a outline so it is still visible if the snakes moves "through" the score"
    def update(self, screen, txt_color, position):
        #draws the outline in black
        font = pygame.font.SysFont("arialblack",55)
        img = font.render(str(self.score),True,(0,0,0))
        screen.blit(img,position)
        #draws the color of the snake
        font = pygame.font.SysFont("arialblack",50)
        img = font.render(str(self.score),True,txt_color)
        screen.blit(img,position)