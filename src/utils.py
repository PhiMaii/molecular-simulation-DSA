import math
import pygame
from pygame import Vector2

def draw_vector(screen: pygame.display, start_pos: Vector2, vector: Vector2, color: tuple, arrow_scale=10, arrow_angle=math.pi / 6):
    end_pos = start_pos + (vector * arrow_scale)

    # Draw the shaft of the arrow
    pygame.draw.line(screen, color, start_pos, end_pos, 2)