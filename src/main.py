import ball

import pygame

import sys
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

num_balls = 15

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Particle Simulation')

balls = [ball.Ball(random.randint(50, screen_width - 50), random.randint(50, screen_height - 50), random.randint(5, 25), RED) for _ in range(num_balls)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    for ball in balls:
        ball.draw(screen)    
    
    pygame.display.flip()

pygame.quit()
sys.exit()
