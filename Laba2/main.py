import pygame
import sys
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(-1,0)
        self.grow = False
    
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(int(x_pos), int(y_pos), cell_size,cell_size)
            pygame.draw.rect(screen, pygame.Color('green'), block_rect)
    
    def move_snake(self):
        if self.grow == False:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.grow = False
    
    def growth(self):
        self.grow = True

class FRUIT:
    def __init__(self):
        # Создаю x и y координаты
        # Рисую квадрат
        self.x = random.randint(0,Cell_Number - 1)
        self.y = random.randint(0,Cell_Number - 1)
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        # Создаю ОВОЩ и рисую его
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple,fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0,Cell_Number - 1)
        self.y = random.randint(0,Cell_Number - 1)
        self.pos = Vector2(self.x,self.y)
 


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.growth()
    
    def check_fail(self):
        if self.snake.body[0].x >= Cell_Number or self.snake.body[0].x < 0  or \
        self.snake.body[0].y >= Cell_Number or self.snake.body[0].y < 0:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()
    
    def draw_score(self):
        text = "ЗМЕЙКА"
        text_surface = game_font2.render(text,False,(255,255,255))
        screen.blit(text_surface, (250,690))
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(255,255,255))
        score_x = int(cell_size * Cell_Number - 60)
        score_y = int(cell_size * Cell_Number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)



pygame.init()
cell_size = 40
Cell_Number = 20
screen = pygame.display.set_mode((cell_size*Cell_Number,cell_size*Cell_Number))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Graphics/impact2.ttf',25)
game_font2 = pygame.font.Font('Graphics/impact2.ttf',100)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.game_over()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and main_game.snake.direction != Vector2(0,-1):
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_UP and main_game.snake.direction != Vector2(0,1):
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_LEFT and main_game.snake.direction != Vector2(1,0):
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT and main_game.snake.direction != Vector2(-1,0):
                main_game.snake.direction = Vector2(1,0)
    screen.fill(pygame.Color('purple'))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
