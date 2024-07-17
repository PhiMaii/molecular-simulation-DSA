import pygame

class Ball:
    def __init__(self, xpos, ypos, radius, color):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.color = color

    def draw(self, screen):
       pygame.draw.circle(screen, self.color, (int(self.xpos), int(self.ypos)), self.radius) 


