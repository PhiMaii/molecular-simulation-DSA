# ---------------------------------- Imports --------------------------------- #
import pygame

import sys
import random

import particle

# --------------------------------- Constants -------------------------------- #
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

NUM_BALLS = 20

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# ------------------------------- Window setup ------------------------------- #
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Particle Simulation')

# ------------------------------ Utility classes ----------------------------- #
def generateBalls(num):
    generated_balls = [particle.Ball(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50), random.randint(5, 25), RED) for _ in range(num)]
    return generated_balls


balls = generateBalls(NUM_BALLS)


# ---------------------------------------------------------------------------- #
#                                   Main loop                                  #
# ---------------------------------------------------------------------------- #
running = True
while running:
    # ------------------------------ Event listeners ----------------------------- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                balls.clear()
                balls.extend(generateBalls(NUM_BALLS)) # append DIDN'T work because only one array is accepted

    # ------------------------------- Update screen ------------------------------ #
    screen.fill(WHITE)

    for ball in balls:
        ball.draw(screen) 

    pygame.display.flip()

# -------------------------------- Exit window ------------------------------- #
pygame.quit()
sys.exit()
