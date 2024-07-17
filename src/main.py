# ---------------------------------- Imports --------------------------------- #
import pygame

import sys
import random

import particle
import config

# ------------------------------- Window setup ------------------------------- #
# Setup of the window: size and description
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Particle Simulation')

# Setup of the FPS counter
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# ------------------------------ Utility classes ----------------------------- #
# Funciton for generating a given amount of randomly placed balls
def generateRandomBalls(num):
    generated_balls = [particle.Ball(random.randint(50, config.SCREEN_WIDTH - 50), random.randint(50, config.SCREEN_HEIGHT - 50), random.randint(5, 25), config.RED) for _ in range(num)]
    return generated_balls


balls = generateRandomBalls(config.NUM_BALLS)


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
                balls.extend(generateRandomBalls(config.NUM_BALLS)) # append DIDN'T work because only one array is accepted
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("Mouse btn down", mouse_x, mouse_y)
                print(particle.Ball(mouse_x, mouse_y, random.randint(5, 25), config.BLUE))
                balls.append(particle.Ball(mouse_x, mouse_y, random.randint(5, 25), config.BLUE))

    # ------------------------------- Update screen ------------------------------ #
    # Erase the screen
    screen.fill(config.WHITE)

    # Every ball gets updated and then drawn
    for ball in balls:
        ball.update()
        ball.draw(screen) 

    # FPS counter display
    fps = int(clock.get_fps())
    fps_text = font.render(f"FPS: {fps}", True, config.BLACK)
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()

    # FPS limit
    clock.tick(config.MAX_FPS)

# -------------------------------- Exit window ------------------------------- #
pygame.quit()
sys.exit()
