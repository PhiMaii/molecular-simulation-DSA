import ball

import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Particle Simulation')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    
    
    pygame.display.flip()

pygame.quit()
sys.exit()
