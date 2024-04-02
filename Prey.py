import pygame
import random

from Settings import *

class Prey:
    def __init__(self, grid_width, grid_height, tilesize, color):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.tilesize = tilesize
        self.color = color
        self.prey_positions = []


    # Draw random
    def spawn_prey(self, prey_count):
        self.prey_positions = []

        for _ in range(prey_count):
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            self.prey_positions.append((x, y))

    def draw_single_prey(self):
        x = random.randint(0, self.grid_width - 1)
        y = random.randint(0, self.grid_height - 1)
        self.prey_positions.append((x, y))

    def move(self):
        for i, (x, y) in enumerate(self.prey_positions):
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_x = (x + dx) % self.grid_width
            new_y = (y + dy) % self.grid_height
            self.prey_positions[i] = (new_x, new_y)

    def draw_prey(self, screen,):
        for position in self.prey_positions:
            x, y = position
            pygame.draw.rect(screen, self.color, (x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize))
