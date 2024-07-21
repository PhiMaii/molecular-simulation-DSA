import pygame
from pygame import Vector2

import newtonutils
import newtonconfig
import LJParticle
from LJParticle import LJParticle
import newtonphysics
import random
# ------------------------------- Window setup ------------------------------- #
# Setup of the window: size and description
pygame.init()
screen = pygame.display.set_mode((newtonconfig.SCR_WIDTH*newtonconfig.SCR_ZOOM, newtonconfig.SCR_HEIGHT*newtonconfig.SCR_ZOOM))
pygame.display.set_caption('Particle Simulation')

# Setup of the FPS counter
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# clock and time
clock = pygame.time.Clock()
time = 0
dt=newtonconfig.TIMESTEP

running = True
parts = []

def initparts():
    for i in range(5):
        for j in range(5):
            parts.append(LJParticle(Vector2(50+i*10,50+j*10),Vector2(400,0).rotate(random.randint(0,360)),0.001,5,newtonconfig.GREEN))

initparts()


interactions = newtonutils.getInteractions(len(parts))
while running:

    # Set backgroundcolor
    screen.fill(newtonconfig.WHITE)

    # Eventlistener for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            parts.append(LJParticle(Vector2(5,5),Vector2(50,50),0.001,5,newtonconfig.GREEN))
            interactions = newtonutils.getInteractions(len(parts))
    # Updating
    for i in range(len(interactions)):
        newtonphysics.lennardJones(parts[interactions[i][0]],parts[interactions[i][1]],dt)
    
    # applying forces and rendering particles
    for i in range(len(parts)):
        parts[i].update(dt)
        parts[i].draw(screen)
    
    time+=dt

    fps_text = font.render(f"Time: {time}", True, newtonconfig.BLACK)
    screen.blit(fps_text, (10, 10))
    pygame.display.flip()