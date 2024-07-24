import pygame
from pygame import Vector2

import utils
import config
import LJParticle
from LJParticle import LJParticle
import physics
import random

# ------------------------------- Window setup ------------------------------- #
# Setup of the window: size and description
pygame.init()
screen = pygame.display.set_mode((config.SCR_WIDTH*config.SCR_ZOOM, config.SCR_HEIGHT*config.SCR_ZOOM))
pygame.display.set_caption('Particle Simulation')

# Setup of the FPS counter
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# clock and time
clock = pygame.time.Clock()
time = 0
dt=config.TIMESTEP
running = True

parts = []

ekin  = 0
def initparts():
    for i in range(10):
        for j in range(10):
            argon=LJParticle(Vector2(0.19+j*0.19,0.19+i*0.19),Vector2(0,0).rotate(random.randint(0,360)),39.948,0.05,config.BLACK)
            parts.append(argon)


initparts()
print(config.SCR_HEIGHT*config.SCR_ZOOM)


interactions = utils.getInteractions(len(parts))
while running:

    # Set backgroundcolor
    screen.fill(config.WHITE)

    # Eventlistener for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Updating
    for i in range(len(interactions)):
        physics.morsePotential(parts[interactions[i][0]],parts[interactions[i][1]],dt)
    
    # applying forces and rendering particles
    for i in range(len(parts)):
        parts[i].update(dt)
        parts[i].draw(screen)
    
    ekin = physics.getKineticEnergy(parts)
    ekin/=6.022*10**26
    
    print("temp:",physics.calculateTemperature(ekin,parts)-273,"°C")

    time+=config.TIMESTEP
    

    fps_text = font.render(f"Time: {time}"+"ns", True, config.BLACK)
    screen.blit(fps_text, (10, 10))
    pygame.display.flip()