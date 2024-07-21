import pygame
from pygame import Vector2

import newtonconfig

class LJParticle:
    # initializing values
    def __init__(self,pos:Vector2, vel:Vector2,mass:float,radius:int,color:tuple):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.radius = radius
        self.color = color
        self.force = Vector2(0)

    # drawing the particle
    def draw(self, screen:pygame.display):
        pygame.draw.circle(screen,self.color,self.pos,self.radius)
    
    def checkcollisions(self):
        if(self.pos.x<self.radius):
            self.pos.x=self.radius
        elif(self.pos.x>newtonconfig.SCR_WIDTH-self.radius):
            self.pos.x = newtonconfig.SCR_WIDTH-self.radius
            self.vel.x*=-1
        if(self.pos.y<self.radius):
            self.pos.y=self.radius
            self.vel.y*=-1
        elif(self.pos.y>newtonconfig.SCR_HEIGHT-self.radius):
            self.pos.y = newtonconfig.SCR_HEIGHT-self.radius
            self.vel.y*=-1
        

    # updating movement based on accumulated force from the previous frame
    def update(self,dt):
        self.checkcollisions()
        self.accel = self.force/self.mass
        self.vel += self.accel
        self.pos+=self.vel*dt
        self.force = Vector2(0)
        print(self.vel.magnitude())
    
    
    
    def applyforce(self,f:Vector2):
        self.force+=f