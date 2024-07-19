import pygame
from pygame import Vector2

import math
import random

import config
import particle

def draw_vector(screen: pygame.display, start_pos: Vector2, vector: Vector2, color: tuple, arrow_scale=2, arrow_angle=math.pi / 6):
    end_pos = start_pos + (vector * arrow_scale)

    # Draw the shaft of the arrow
    pygame.draw.line(screen, color, start_pos, end_pos, 2)

def calcImpulse (m1, v1, m2, v2):
    vn = (m1 * v1 + m2 * (2 * v2 - v1)) / (m1 + m2)
    return vn

# Function for generating a given amount of randomly placed balls
def generateRandomBalls(num: int):
    generated_balls= []
    for i in range(num):
        pos = Vector2(random.randint(50, config.SIMULATION_WIDTH - 50),random.randint(50, config.SCREEN_HEIGHT - 50))
        vel = Vector2(0)
        mass = 1
        generated_ball = particle.Ball(pos, vel, mass, random.randint(config.BALL_SIZE_RANGE[0], config.BALL_SIZE_RANGE[1]), config.RED)
        generated_balls.append(generated_ball)
    return generated_balls

# Function to generate two balls heading straight to each other (for debugging purposes)
def generateTestBalls():
    generated_balls = [
        particle.Ball(pos=Vector2(100, 200), mass=1, vel=Vector2(15, 0), radius=15, color=config.RED),
        particle.Ball(pos= Vector2(config.SIMULATION_WIDTH - 100, 200), vel=Vector2(0, 0), mass=1, radius= 15, color=config.GREEN)
    ]
    return generated_balls

def generateGasParticles():
    generated_balls = []
    for _ in range(config.NUM_BALLS):
        pos = Vector2(random.randint(50, config.SIMULATION_WIDTH - 50), random.randint(50, config.SCREEN_HEIGHT - 50))
        # vel = Vector2(random.randint(-20, 20), random.randint(-20, 20))
        random_vels = [15, -15]
        vel = Vector2(random.choice(random_vels), random.choice(random_vels))
        mass = 1
        color = config.RED

        generated_ball = particle.Ball(vel=vel, pos=pos, radius=7, mass=mass, color=color)

        generated_balls.append(generated_ball)
    return generated_balls