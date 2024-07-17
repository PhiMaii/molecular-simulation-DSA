import pygame

import sys
import random

import particle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

NUM_BALLS = 20

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Particle Simulation')

def generateBalls(num):
    generated_balls = [particle.Ball(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50), random.randint(5, 25), RED) for _ in range(num)]
    return generated_balls

balls = generateBalls(NUM_BALLS)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                balls.clear()
                balls.extend(generateBalls(NUM_BALLS))


                print("pressed")
                # balls.pop(-1)

    screen.fill(WHITE)

    for ball in balls:
        ball.draw(screen) 


    pygame.display.flip()

pygame.quit()
sys.exit()
