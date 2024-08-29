# window
TILEWIDTH = 16
TILEHEIGHT = 16
NROWS = 36
NCOLS = 28
SCREENWIDTH = NCOLS * TILEWIDTH
SCREENHEIGHT = NROWS * TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
WINDOWTITLE = "Erikão's Pacman"

# maze path
MAZEPATH = "src/assets/maze.txt"
ROTATIONPATH = "src/assets/maze_rotation.txt"

# font path
FONTPATH = "src/assets/PressStart2P-Regular.ttf"

# sprits path
SPRITEPATH = "src/assets/spritesheet.png"

# directions
STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2
PORTAL = 3
DEATH = 5

# characters and elements
PACMAN = 0
PELLET = 1
POWERPELLET = 2
GHOST = 3
BLINKY = 4
PINKY = 5
INKY = 6
CLYDE = 7
FRUIT = 8

# ghosts modes
SCATTER = 0
CHASE = 1
FREIGHT = 2
SPAWN = 3

# colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255,100,150)
TEAL = (100,255,255)
ORANGE = (230,190,40)
BLUE = (65, 105, 225)
GREEN = (0, 255, 0)

# text
SCORETXT = 0
LEVELTXT = 1
READYTXT = 2
PAUSETXT = 3
GAMEOVERTXT = 4
