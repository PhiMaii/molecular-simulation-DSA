import pygame
from pygame import Vector2

import config


class Ball:
    def __init__(self, pos: Vector2, vel: Vector2, radius: int, color: tuple):
        # Initialise class variables
        
        self.radius = radius
        self.color = color

        self.pos = pos
        self.vel = vel

    def draw(self, screen):
       # Draw the circle on the screen
       pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius) 

    def update(self):
        # Adding gravity factor to the y velocity on each update call
        self.vel.y += config.GRAVITY

        # Multiplying both velocities by the friction coefficient
        self.vel.y *= config.FRICTION
        self.vel.x *= config.FRICTION

        # Adding the current velocity to the position of the corresponding axis
        self.pos+=self.vel

        self.checkWallCollision()

    def checkWallCollision(self):
        # Checking for collisions with the window edges and resolving them
        # Left side
        if self.pos.x - self.radius < 0:
            self.pos.x = self.radius
            self.vel.x *= -1
        # Right side
        elif self.pos.x + self.radius > config.SCREEN_WIDTH:
            self.pos.x = config.SCREEN_WIDTH - self.radius
            self.vel.x *= -1

        # Top side
        if self.pos.y - self.radius < 0:
            self.pos.y = self.radius
            self.vel.y *= -1
        # Bottom side
        elif self.pos.y + self.radius > config.SCREEN_HEIGHT:
            self.pos.y = config.SCREEN_HEIGHT - self.radius
            self.vel.y *= -1

