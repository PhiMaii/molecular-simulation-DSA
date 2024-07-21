# ---------------------------------- Imports --------------------------------- #
import pygame
from pygame import Vector2
import pygame_gui

import sys
import random
import time

import particle
import config
import utils
from ui import GUI

# ------------------------------- Window setup ------------------------------- #
# Setup of the window: size and description
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Particle Simulation')

# UI manager setup
manager = pygame_gui.UIManager((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
gui = GUI(manager)

# Setup of the FPS counter
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# ------------------------------ Utility classes ----------------------------- #
if config.DEBUG_MODE:
    balls = utils.generateTestBalls()
else:
    # balls = utils.generateRandomBalls(config.NUM_BALLS)
    balls = utils.generateGasParticles()

# ---------------------------------------------------------------------------- #
#                                   Main loop                                  #
# ---------------------------------------------------------------------------- #
running = True

single_step = False

last_time = time.time()

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
                if not config.paused:
                    config.paused = True
                else:
                    config.paused = False
                print(config.paused)
            if event.key == pygame.K_SPACE:
                single_step = not single_step
                
        # Mouse button pressed event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left-click pressed
            if event.button == 1:
                # Spawn a new ball at the mouse's coordinates
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # balls.append(particle.Ball(pos=Vector2(mouse_x, mouse_y),mass=15 , radius=20, vel=Vector2(0,0), color=config.BLUE))
            elif event.button == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # balls.append(particle.Ball(pos=Vector2(mouse_x, mouse_y),mass=2 , radius=20, vel=Vector2(0,0), color=config.GREEN))

        gui.process_events(event)


    config.temperature = gui.temperature_slider.current_value

    # ------------------------------- Update screen ------------------------------ #
    # Erase the screen
    screen.fill(config.WHITE)

    dt = time.time() - last_time
    last_time = time.time()
    # print(dt)

    pygame.draw.rect(screen, (225, 225, 225), (config.SIMULATION_WIDTH, 0, config.MENU_WIDTH, config.SCREEN_HEIGHT))
    gui.update(dt)

    if(config.paused):
        for ball in balls:
            ball.draw(screen)
    
    elif(not config.paused):
        # Iterate through each ball and first update, then check for collisions and then draw it
        for i, ball in enumerate(balls):
            ball.update(dt)
            for j in range(i + 1, len(balls)):
                ball.collide(balls[j])
            ball.draw(screen)

    gui.draw(screen)


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