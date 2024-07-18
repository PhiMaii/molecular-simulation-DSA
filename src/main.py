# ---------------------------------- Imports --------------------------------- #
import pygame
from pygame import Vector2

import sys
import random

import particle
import config
import utils

# ------------------------------- Window setup ------------------------------- #
# Setup of the window: size and description
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Particle Simulation')

# Setup of the FPS counter
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# ------------------------------ Utility classes ----------------------------- #
if config.DEBUG_MODE:
    balls = utils.generateTestBalls()
else:
    balls = utils.generateRandomBalls(config.NUM_BALLS)

# ---------------------------------------------------------------------------- #
#                                   Main loop                                  #
# ---------------------------------------------------------------------------- #
running = True
paused = False

last_time = pygame.time.get_ticks()

while running:
    # ------------------------------ Event listeners ----------------------------- #
    for event in pygame.event.get():
        # Window close event
        if event.type == pygame.QUIT:
            running = False
        # Key pressed event
        elif event.type == pygame.KEYDOWN:
            # Pressed key is "r"
            if event.key == pygame.K_r:
                # Delete all balls and generate new ones (random)
                balls.clear()
                balls.extend(utils.generateRandomBalls(config.NUM_BALLS)) # append DIDN'T work because only one array is accepted
            if event.key == pygame.K_p:
                if not paused:
                    paused = True
                else:
                    paused = False
                print(paused)
        # Mouse button pressed event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left-click pressed
            if event.button == 1:
                # Spawn a new ball at the mouse's coordinates
                mouse_x, mouse_y = pygame.mouse.get_pos()
                balls.append(particle.Ball(pos=Vector2(mouse_x, mouse_y),mass=50 , radius=20, vel=Vector2(0,0), color=config.BLUE))
            elif event.button == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                balls.append(particle.Ball(pos=Vector2(mouse_x, mouse_y),mass=2 , radius=20, vel=Vector2(0,0), color=config.BLUE))


    # ------------------------------- Update screen ------------------------------ #
    # Erase the screen
    screen.fill(config.WHITE)

    # dt = clock.get_time() / config.TIME_FACTOR

    current_time = pygame.time.get_ticks()
    dt = (current_time - last_time) / config.TIME_FACTOR # Convert milliseconds to seconds
    last_time = current_time

    # print(dt)

    # Iterate through each ball and first update, then check for collisions and then draw it
    for i, ball in enumerate(balls):
        ball.update(dt)
        for j in range(i + 1, len(balls)):
            ball.collide(balls[j])
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