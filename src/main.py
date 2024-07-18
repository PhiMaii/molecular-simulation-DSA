# ---------------------------------- Imports --------------------------------- #
import pygame
from pygame import Vector2

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
# Function for generating a given amount of randomly placed balls
def generateRandomBalls(num):
    generated_balls= []
    for i in range(num):
        pos = Vector2(random.randint(50, config.SCREEN_WIDTH - 50),random.randint(50, config.SCREEN_HEIGHT - 50))
        vel = Vector2(0)
        generated_ball = particle.Ball(pos, vel, random.randint(5, 25), config.RED)
        generated_balls.append(generated_ball)
    return generated_balls


# balls = generateRandomBalls(config.NUM_BALLS)


def generateTestBalls():
    generated_balls = [
        particle.Ball(pos=Vector2(100, 200), vel=Vector2(10, 0), radius=15, color=config.RED),
        particle.Ball(pos= Vector2(config.SCREEN_WIDTH - 100, 200), vel=Vector2(-10, 0), radius= 15, color=config.GREEN)
    ]
    return generated_balls

balls = generateTestBalls()


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
                balls.extend(generateTestBalls()) # append DIDN'T work because only one array is accepted
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                balls.append(particle.Ball(pos=Vector2(mouse_x, mouse_y), radius=random.randint(5, 25), vel=Vector2(20,5), color=config.BLUE))

    # ------------------------------- Update screen ------------------------------ #
    # Erase the screen
    screen.fill(config.WHITE)

    # Every ball gets updated and then drawn
    # for ball in balls:
    #     ball.update()
    #     ball.draw(screen) 

    for i, ball in enumerate(balls):
        ball.update()
        for j in range(i + 1, len(balls)):
            ball.collide(balls[j], screen)
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
