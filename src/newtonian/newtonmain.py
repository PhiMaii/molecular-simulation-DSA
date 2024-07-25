import pygame
from pygame import Vector2

import newtonutils
import newtonconfig
import LJParticle
from LJParticle import LJParticle
import newtonphysics
import random
import pylab as plt


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
    for i in range(10):
        for j in range(10):
            argon1=LJParticle(Vector2(0.1+i*0.2,0.1+0.2*j),Vector2(50*i,50*j).rotate(random.randint(0,360)),39.948,0.098,newtonconfig.BLACK,[])
            #argon2=LJParticle(Vector2(0.2+i*0.2,0.2+0.2*j),Vector2(430,0).rotate(random.randint(0,360)),39.948,0.098,newtonconfig.BLUE,[argon1])
            #parts.append(argon2)
            parts.append(argon1)
    
        
    
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
    minV=parts[0].vel.magnitude()
    maxV=parts[0].vel.magnitude()
    maxW = newtonconfig.SCR_WIDTH
    maxH = newtonconfig.SCR_HEIGHT

    for i in range(len(parts)):
        #if(parts[i].vel.magnitude()>maxV):
        #    maxV=parts[i].vel.magnitude()
        #if(parts[i].vel.magnitude()<minV):
        #    minV=parts[i].vel.magnitude()
        r = parts[i].pos.x/maxW*255
        g = parts[i].pos.y/maxH*255
        color=(r,g,255)
        parts[i].color=color
        
    step = (maxV-minV)/255
    print("min",minV)
    print("max",maxV)
    print("step:",step)
    cmap = plt.get_cmap("jet")
    
    for i in range(len(parts)):
        #velFactor = ((parts[i].vel.magnitude()-minV)/step)
        #print("minus",parts[i].vel.magnitude()-minV)
        #print(velFactor)
        #color = cmap(parts[i].vel.magnitude()/maxV)
        print(color)

        #parts[i].color= (color[0]*255,color[1]*255,color[2]*255)
        parts[i].draw(screen)
        parts[i].update(dt)
    ekin = newtonphysics.getKineticEnergy(parts)
    ekin/=6.022*10**26
    
    print("temp:",newtonphysics.calculateTemperature(ekin,parts)-273,"°C")

    time+=newtonconfig.TIMESTEP
    

    fps_text = font.render(f"Time: {time}"+"ns", True, newtonconfig.BLACK)
    #screen.blit(fps_text, (10, 10))
    pygame.display.flip()