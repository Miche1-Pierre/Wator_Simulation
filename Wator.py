import pygame, sys

from Settings import *
from Grid import *
from Prey import *
from Shark import *

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
shark_random = Shark(X_GRID, Y_GRID, TILESIZE, SHARK_COLOR, INITIAL_SHARK_ENERGY, BREEDING_THRESHOLD, ENERGY_LOSS_RATE)
shark_random.spawn_shark(SHARK_INITIAL_COUNT)

# Temps écoulé depuis la dernière naissance d'un requin
time_since_last_shark_breed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(SCREEN_COLOR)

    grid.draw_grid(screen)

    prey_random.move()
    prey_random.draw_prey(screen)
    for _ in range(PREY_SPAWN_RATE):
        prey_random.draw_single_prey()

    shark_random.move()
    shark_random.eat_fish(prey_random.prey_positions)
    shark_random.breed()
    shark_random.update_energy()
    shark_random.draw_sharks(screen)



    pygame.display.flip()

pygame.quit()