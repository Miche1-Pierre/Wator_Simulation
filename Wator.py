import pygame, sys

from Settings import *
from Grid import *
from Prey import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wator Simulation")

# Grid
grid = Grid(X_GRID, Y_GRID, TILESIZE)
grid.set_color(GRID_COLOR)

# Prey
prey_random = Prey(X_GRID, Y_GRID, TILESIZE, PREY_COLOR)
prey_random.spawn_prey(PREY_INITIAL_COUNT)

# Temps écoulé depuis la dernière naissance de proie
time_since_last_breed = 0

# Predator

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(SCREEN_COLOR)

    grid.draw_grid(screen)

    prey_random.move()  # Faire bouger les proies
    prey_random.draw_prey(screen)  # Dessiner les proies
    for _ in range(PREY_SPAWN_RATE):
        prey_random.draw_single_prey()


    pygame.display.flip()

pygame.quit()