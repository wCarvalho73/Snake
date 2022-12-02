from enum import Enum

import pygame as pg

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Snake:
    def __init__(self, color: tuple, inicial_direction:Direction, 
                inicial_body: list[tuple], surface:pg.Surface) -> None:

        self.body = inicial_body
        self.color = color
        self.direction = inicial_direction
        self.surface = surface
        self.square_size = 10


    def event_listener(self, event) -> None:
        key = event.key
        if key == pg.K_UP:
               self.direction = Direction.UP
        elif key == pg.K_DOWN:
               self.direction = Direction.DOWN
        elif key == pg.K_LEFT:
               self.direction = Direction.LEFT
        elif key == pg.K_RIGHT:
               self.direction = Direction.RIGHT
    
    def draw(self) -> None:
        for square in self.body:
            rect = (square,(self.square_size, self.square_size))
            pg.draw.rect(self.surface, self.color, rect)
        
    def update(self) -> None:
        for i in range(len(self.body)-1,0,-1):
            self.body[i]=(self.body[i-1][0],self.body[i-1][1])

        if self.direction == Direction.UP:
            self.body[0] = (self.body[0][0], self.body[0][1] - 10)
        elif self.direction == Direction.DOWN:
             self.body[0] = ( self.body[0][0], self.body[0][1] + 10)
        elif self.direction == Direction.LEFT:
             self.body[0] = ( self.body[0][0] - 10, self.body[0][1])
        elif self.direction == Direction.RIGHT:
             self.body[0] = ( self.body[0][0] + 10, self.body[0][1])
        
        
