import pygame
import random

from Settings import *

class Shark:
    def __init__(self, grid_width, grid_height, tilesize, color, initial_energy, breeding_threshold, energy_loss_rate):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.tilesize = tilesize
        self.color = color
        self.shark_positions = []
        self.energy = initial_energy
        self.breeding_threshold = breeding_threshold
        self.energy_loss_rate = energy_loss_rate

    def spawn_shark(self, shark_count):
        self.shark_positions = []

        for _ in range(shark_count):
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            self.shark_positions.append((x, y))

    def draw_single_shark(self):
        x = random.randint(0, self.grid_width - 1)
        y = random.randint(0, self.grid_height - 1)
        self.shark_positions.append((x, y))

    def draw_sharks(self, screen):
        for position in self.shark_positions:
            x, y = position
            pygame.draw.rect(screen, self.color, (x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize))

    def move(self):
        for i, (x, y) in enumerate(self.shark_positions):
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_x = (x + dx) % self.grid_width
            new_y = (y + dy) % self.grid_height
            self.shark_positions[i] = (new_x, new_y)

    
    def eat_fish(self, prey_positions):
        eaten_fish = []
        for position in self.shark_positions:
            if position in prey_positions:
                eaten_fish.append(position)
                prey_positions.remove(position)  # Supprime la proie consommée de la liste des positions des proies
                self.energy += ENERGY_GAIN_FROM_FISH

    def breed(self):
        if self.energy >= self.breeding_threshold:
            for x, y in self.shark_positions[:]:
                possible_birth_spots = [(x + dx, y + dy) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]]
                for spot in possible_birth_spots:
                    if spot not in self.shark_positions:
                        self.shark_positions.append(spot)
                        self.energy //= 2

    def update_energy(self):
        self.energy -= self.energy_loss_rate