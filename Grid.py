import pygame

from Settings import *

class Grid:
    def __init__(self, X, Y, tilesize):
        self.X = X
        self.Y = Y
        self.tilesize = tilesize
        self.grid_data = [[None] * X for _ in range(Y)]

    def set_color(self, color):
        self.color = color
    
    def draw_grid(self, screen):
        for i in range(1, self.X):
            pygame.draw.line(screen, self.color, (self.tilesize * i, 0), (self.tilesize * i, self.tilesize * self.X))
        for j in range(1, self.Y):
            pygame.draw.line(screen, self.color, (0, self.tilesize * i), (self.tilesize * self.X, self.tilesize * i))


        for y in range(self.Y):
            for x in range(self.X):
                if self.grid_data[y][x] == 'prey':
                    pygame.draw.circle(screen, PREY_COLOR, (x * self.tilesize + self.tilesize // 2, y * self.tilesize + self.tilesize // 2), self.tilesize // 2)

    def is_valid_move(self, X, Y):
        return 0 <= X < self.X and 0 <= Y < self.Y and self.grid_data[Y][X] is None
    
    def get_empty_neighbors(self, X, Y):
        empty_neighbors = []
        for dX, dY in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_X, new_Y = X + dX, Y + dY
            if self.is_valid_move(new_X, new_Y):
                empty_neighbors.append((new_X, new_Y))
        return empty_neighbors
    
    def add_prey(self, X, Y):
        self.grid_data[X][Y] = 'prey'

