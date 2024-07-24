import pygame
from pygame import Vector2

import config

class LJParticle:
    # initializing values
    def __init__(self,pos:Vector2, vel:Vector2,mass:float,radius:int,color:tuple):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.radius = radius
        self.color = color
        self.ekin = 0.5*self.mass*self.vel.magnitude()**2
        self.force = Vector2(0)

    # drawing the particle
    def draw(self, screen:pygame.display):
        pygame.draw.circle(screen,self.color,self.pos*config.SCR_ZOOM,self.radius*config.SCR_ZOOM)

    def checkcollisions(self):
        if(self.pos.x<self.radius):
            self.pos.x=self.radius
            self.vel.x*=-1
        elif(self.pos.x>config.SCR_WIDTH-self.radius):
            self.pos.x = config.SCR_WIDTH-self.radius
            self.vel.x*=-1
        if(self.pos.y<self.radius):
            self.pos.y=self.radius
            self.vel.y*=-1
        elif(self.pos.y>config.SCR_HEIGHT-self.radius):
            self.pos.y = config.SCR_HEIGHT-self.radius
            self.vel.y*=-1
        

    # updating movement based on accumulated force from the previous frame
    def update(self,dt):
        self.checkcollisions()

        self.accel = self.force/self.mass

        self.vel += self.accel
        self.pos+=self.vel*dt

        self.ekin = 0.5*self.mass*self.vel.magnitude()**2
        
        self.force = Vector2(0)
    
    def applyforce(self,f:Vector2):
        self.force+=f