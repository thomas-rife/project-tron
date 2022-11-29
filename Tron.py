"""
The tron game.
Brian, Thomas, Robert
"""
import pygame, sys
pygame.init()

#color
BLUE = (0, 0, 50)

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

    'draws a starting snake at opposite positions'
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
    
    'adds a block to the existing snake in the given direction - just draws over the existing shape'
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

    def die(self):
        snake.headx = random.randrange(0, width)
        snake.heady = random.randrange(0, hieght)
        "should be how the snake respawns, but this part still needs to be rewokred"

class game:

    def __init__(self, height, width, difficulty):
        self.height = height
        self.width = width   
        self.difficulty = difficulty

    'makes the screen'
    def create_screen(self):
        screen = pygame.display.set_mode([self.height, self.width])
        pygame.display.set_caption('Tron') 
        screen.fill((255,255,255))
        return screen
    'didnt get this to work, but this is how one would add images to the screen for the start and end'    
    def add_background(self, image):
        background = pygame.image.load(image)
        #back_rect = background.get_rect()

    'draws the grid for the game, 20 by 20'
    def draw_grid(self, screen):
        x_value = 0
        y_value = 0
        for x in range(20):
            for y in range(20):
                pygame.draw.rect(screen, (0,0,0), [x_value, y_value, self.width/20, self.height/20], 3)
                y_value += self.height/20
            x_value += self.width/20
            y_value = 0
    
    'this is what is called to start the game'
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
                    direction = player1.player_input(event)
                    direction2 = (player2.player_input(event))

            snake1.extend_snake(direction)
            snake2.extend_snake(direction2)
            pygame.display.update()
            pygame.time.wait(self.difficulty)

if collision.between_snakes(self, snake1, snake2):
    snake.extend_snake()
if collision.between_snake_and_walls(snake):
    #lose
    snake.die()
    #reset score (score=0)



    def display_label(self, message):
        """ this is where we define the display label to put the introductory message before game starts
        """
        
    def starter_message(self):
        self.display_label('', 3) #insert title for game here 
        self.display_label('Your game starts in \n 3', 1)
        self.display_label('Your game starts in \n 2', 1)
        self.display_label('Your game starts in \n 1', 1)

class collision:
    def between_snakes(self, snake1, snake2):
        if snake1.x < snake2.x + snake1.w and snake1.x + snake1.w > snake2.x and snake1.y < snake1.y + snake2.h and snake1.y + snake1.h > snake2.y:
            return True
        else:
            return False  
    def between_snake_and_walls(self, snake):
        if snake.headx < 0 or snake.headx > width or snake.heady < 0 or snake.heady > height:
            return True
        else:
            return False
    def between_head_and_body(self, snake):
        for body in snake.extend
        # this should for when user collides with the body of its own snake
        # stil needs to be finished

class score:
    def __init__(self):
        self.points = 0
        self.font = pygame.font.SysFont('monospace', 20, bold=False)

    def increase(self):
        self.points += 1

    def reset(self):
        self.points = 0 
    
    def show(self, surface):
        label = self.font.render('Score: ' + str(self.points), 1 , BLUE)

class player:
    'need to get the users inputs and keep track of their scores'
    def __init__(self, score, keys, snake, dir):
        self.score = score
        self.keys = keys
        self.snake = snake
        self.dir = dir
        score = 0 
    'returns the direction the snake should move depending on the key pressed'
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