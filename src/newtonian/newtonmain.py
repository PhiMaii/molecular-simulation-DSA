import pygame
from pygame import Vector2

import newtonconfig
import LJParticle
from LJParticle import LJParticle
# ------------------------------- Window setup ------------------------------- #
# Setup of the window: size and description
pygame.init()
screen = pygame.display.set_mode((newtonconfig.SCR_WIDTH, newtonconfig.SCR_HEIGHT))
pygame.display.set_caption('Particle Simulation')

# Setup of the FPS counter
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# clock and time
clock = pygame.time.Clock()
time = 0
dt=0

running = True


testpart = LJParticle.LJParticle(Vector2(20,20),Vector2(20,20),10,10,newtonconfig.GREEN)

while running:

    # Set backgroundcolor
    screen.fill(newtonconfig.WHITE)

    # Eventlistener for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating

    # Rendering
    testpart.draw(screen)
    
    #getting dt from the clock (in Milliseconds), dividing it by 1000 to get seconds and multiplying it by the timefactor
    dt = clock.tick()/1000*newtonconfig.TIMEFACTOR
    time+=dt
    pygame.display.flip()