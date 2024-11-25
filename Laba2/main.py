import pygame
import sys
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        # Создаю x и y координаты
        # Рисую квадрат
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        # Создаю ОВОЩ и рисую его
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        pygame.draw.rect(screen, pygame.Color('red'), fruit_rect)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock = pygame.time.Clock()

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color('purple'))
    fruit.draw_fruit()

    pygame.display.update()
    clock.tick(60)