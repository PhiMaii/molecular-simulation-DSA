import pygame
from pygame import Vector2

import config
import utils


class Ball:
    def __init__(self, pos: Vector2, vel: Vector2, mass: int, radius: int, color: tuple):
        # Initialise class variables
        
        self.radius = radius
        self.color = color

        self.pos = pos
        self.vel = vel
        self.acc = Vector2(0, 0)
        self.mass = mass

    def apply_force(self, force):
        # Newton's second law: F = m * a => a = F / m
        self.acc += force / self.mass

    def draw(self, screen: pygame.surface):
        """
        Function that draws the ball on the screen
        """
        # Draw the circle on the screen
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius) 

        if config.DEBUG_MODE:
            utils.draw_vector(screen, self.pos, self.vel, config.BLACK)

    def update(self, dt):
        """
        Updates the possition of the ball
        """
        # Apply gravity force
        gravity_force = Vector2(0, config.GRAVITY * self.mass)
        self.apply_force(gravity_force)

        # Update velocity and position using the current acceleration
        self.vel += self.acc * dt * config.TIME_FACTOR
        self.pos += self.vel * dt * config.TIME_FACTOR

        self.vel *= config.FRICTION

        # Reset acceleration after each update
        self.acc = Vector2(0, 0)

        self.checkWallCollision()

    def checkWallCollision(self):
        """
        Checks for wall collisions and resolves them by multiplying the velocity with -1
        thus reversing the direction and speed
        """
        # Checking for collisions with the window edges and resolving them
        # Left side
        if self.pos.x - self.radius < 0:
            self.pos.x = self.radius
            self.vel.x *= -1

        # Right side
        elif self.pos.x + self.radius > config.SIMULATION_WIDTH:
            self.pos.x = config.SIMULATION_WIDTH - self.radius
            self.vel.x *= -1

        # Top side
        if self.pos.y - self.radius < 0:
            self.pos.y = self.radius
            self.vel.y *= -1

        # Bottom side
        elif self.pos.y + self.radius > config.SCREEN_HEIGHT:
            self.pos.y = config.SCREEN_HEIGHT - self.radius
            self.vel.y *= -1

    def collide(self, other: 'Ball'):
        # Calculate the distance between the two balls
        distance = self.pos.distance_to(other.pos)

        if (not distance < self.radius + other.radius):
            return
        
        # Calculate the normal and tangent vectors
        normal = other.pos - self.pos
        normal = normal.normalize()
        tangent = Vector2(-normal.y, normal.x)

        overlap = self.radius + other.radius - distance
        if overlap > 0:
            self.pos -= normal * overlap / 2
            other.pos += normal * overlap / 2

        # Decompose velocities into normal and tangential components
        v1_normal = normal.dot(self.vel)
        v2_normal = normal.dot(other.vel)
        v1_tangent = tangent.dot(self.vel)
        v2_tangent = tangent.dot(other.vel)

        # Calculate new normal velocities after collision
        v1_normal_new = (v1_normal * (self.mass - other.mass) + 2 * other.mass * v2_normal) / (self.mass + other.mass)
        v2_normal_new = (v2_normal * (other.mass - self.mass) + 2 * self.mass * v1_normal) / (self.mass + other.mass)

        # Convert scalar normal and tangential velocities into vectors
        self.vel = v1_normal_new * normal + v1_tangent * tangent
        other.vel = v2_normal_new * normal + v2_tangent * tangent