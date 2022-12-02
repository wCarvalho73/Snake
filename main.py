from src.snake import Snake,Direction
from src.apple import Apple

import pygame as pg

pg.init()
pg.display.set_caption("snake-game")
screen = pg.display.set_mode((900,600))
clock = pg.time.Clock()
FPS = 10

body = [(200,200),(210,200),(220,200)]
snake = Snake(
    color=(0,128,0),
    inicial_direction=Direction.RIGHT,
    inicial_body=body,
    surface=screen
)

apple = Apple(
    color=(255,0,0),
    surface=screen,
    grid_size=(900,600)
)

apple.new_position(snake.body)

while True:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            snake.event_listener(event)

    if apple.collide(snake.body[0]):
        snake.body.append((0,0))
        apple.new_position(snake.body) 
    
    snake.update()
    screen.fill((0,0,0))
    
    apple.draw()
    snake.draw()
    pg.display.update()