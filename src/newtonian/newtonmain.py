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

ekin  = 0
def initparts():
    #argon1=LJParticle(Vector2(10.38,10),Vector2(0),39.948*newtonconfig.U,0.1,newtonconfig.BLACK)
    #argon2=LJParticle(Vector2(10,10),Vector2(0),39.948*newtonconfig.U,0.1,newtonconfig.BLACK)
    #argon3=LJParticle(Vector2(10,10.38),Vector2(0),39.948*newtonconfig.U,0.1,newtonconfig.BLACK)
    #parts.append(argon1)
    #parts.append(argon2)
    #parts.append(argon3)
    for i in range(3):
        for j in range(3):
            argon=LJParticle(Vector2(0.38+j*0.38,0.38+i*0.38),Vector2(0,0).rotate(random.randint(0,360)),39.948,0.19,newtonconfig.BLACK)
            parts.append(argon)


initparts()
print(newtonconfig.SCR_HEIGHT*newtonconfig.SCR_ZOOM)


interactions = newtonutils.getInteractions(len(parts))
while running:

    # Set backgroundcolor
    screen.fill(newtonconfig.WHITE)

    # Eventlistener for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Updating
    for i in range(len(interactions)):
        newtonphysics.lennardJones(parts[interactions[i][0]],parts[interactions[i][1]],dt)
    
    # applying forces and rendering particles
    for i in range(len(parts)):
        parts[i].update(dt)
        parts[i].draw(screen)
    
    ekin = newtonphysics.getKineticEnergy(parts)
    print(parts[0].vel)
    
    time+=dt

    fps_text = font.render(f"Time: {time}"+"ns", True, newtonconfig.BLACK)
    screen.blit(fps_text, (10, 10))
    pygame.display.flip()