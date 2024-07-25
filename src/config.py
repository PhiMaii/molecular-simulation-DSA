# DEBUG Mode
DEBUG_MODE = False
show_vels = False

# Window setup
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

SIMULATION_WIDTH = int(SCREEN_WIDTH / 3 * 2)
MENU_WIDTH = SCREEN_WIDTH - SIMULATION_WIDTH

# Simulation settings
MAX_FPS = 120
TIME_FACTOR = 15

# Color setup
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Particle setup
NUM_BALLS = 60
BALL_SIZE_RANGE = [15, 25]
ball_size = 7

# Physics setup
GRAVITY = 0
FRICTION = 1
temperature = 1


# ------------------------------ State Variables ----------------------------- #
paused = False

