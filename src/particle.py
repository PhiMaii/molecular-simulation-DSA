import pygame

import config


class Ball:
    def __init__(self, xpos, ypos, radius, color):
        # Initialise class variables
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.color = color

        self.vx = 0
        self.vy = 0

    def draw(self, screen):
       # Draw the circle on the screen
       pygame.draw.circle(screen, self.color, (int(self.xpos), int(self.ypos)), self.radius) 

    def update(self):
        # Adding gravity factor to the y velocity on each update call
        self.vy += config.GRAVITY

        # Multiplying both velocities by the friction coefficient
        self.vy *= config.FRICTION
        self.vx *= config.FRICTION

        # Adding the current velocity to the position of the corresponding axis
        self.xpos += self.vx
        self.ypos += self.vy

        # Checking for collisions with the window edges and resolving them
        # Left side
        if self.xpos - self.radius < 0:
            self.xpos = self.radius
            self.vx *= -1
        # Right side
        elif self.xpos + self.radius > config.SCREEN_WIDTH:
            self.xpos = config.SCREEN_WIDTH - self.radius
            self.vx *= -1

        # Top side
        if self.ypos - self.radius < 0:
            self.ypos = self.radius
            self.vy *= -1
        # Bottom side
        elif self.ypos + self.radius > config.SCREEN_HEIGHT:
            self.ypos = config.SCREEN_HEIGHT - self.radius
            self.vy *= -1

