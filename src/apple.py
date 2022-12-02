import pygame as pg

import random

class Apple:
    def __init__(self, color: tuple, surface: pg.Surface, grid_size: tuple) -> None:
        self.color = color
        self.surface = surface
        self.square_size = 10
        self.grid_size = grid_size
        self.position = (0,0)

    def collide(self, position) -> bool:
        return self.position[0] == position[0] and self.position[1] == position[1]


    def random_position(self) -> tuple:
        x = random.randint(0,self.grid_size[0])
        y = random.randint(0,self.grid_size[1])
        return(x//self.square_size * self.square_size,y//self.square_size * self.square_size)
    
    def new_position(self, snake_body) -> None:
        new_position = self.random_position()

        while new_position in snake_body:
            new_position = self.random_position()

        self.position = new_position
    
    def draw(self) -> None:
        rect = (self.position,(self.square_size,self.square_size))
        pg.draw.rect(self.surface, self.color, rect)

