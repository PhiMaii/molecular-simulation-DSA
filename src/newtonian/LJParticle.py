import pygame
from pygame import Vector2

class LJParticle:
    def __init__(self,pos:Vector2, vel:Vector2,mass:float,radius:int,color:tuple):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.radius = radius
        self.color = color

    def draw(self, screen:pygame.display):
        pygame.draw.circle(screen,self.color,self.pos,self.radius)
    
    def update(dt):
        