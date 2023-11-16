# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 800
HEIGHT = 700
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (175, 100, 50, 20, "normal")]

MOB_LIST = [(0, HEIGHT - 40, WIDTH, 40, "moving vertically"),
            (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"moving horizontally"),
            (125, HEIGHT - 350, 100, 20, "moving vertically"),
            (222, 200, 100, 20, "moving vertically"),
            (175, 100, 50, 20, "moving horizontally")]

# [(0, HEIGHT - 40, WIDTH, 40, "moving"),
#             (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, "moving"),
#             (125, HEIGHT - 350, 100, 20, "moving"),
#             (222, 200, 100, 20, "moving"),
#             (175, 100, 50, 20, "moving")]