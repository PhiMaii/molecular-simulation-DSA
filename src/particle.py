import pygame

import config


class Ball:
    def __init__(self, xpos, ypos, radius, color):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.color = color

        self.vx = 0
        self.vy = 0

    def draw(self, screen):
       pygame.draw.circle(screen, self.color, (int(self.xpos), int(self.ypos)), self.radius) 

    def update(self):
        self.vy += config.GRAVITY

        self.xpos += self.vx
        self.ypos += self.vy

        if self.xpos - self.radius < 0:
            self.xpos = self.radius
            self.vx *= -1
        elif self.xpos + self.radius > config.SCREEN_WIDTH:
            self.xpos = config.SCREEN_WIDTH - self.radius
            self.vx *= -1

        if self.ypos - self.radius < 0:
            self.ypos = self.radius
            self.vy *= -1
        elif self.ypos + self.radius > config.SCREEN_HEIGHT:
            self.ypos = config.SCREEN_HEIGHT - self.radius
            self.vy *= -1

