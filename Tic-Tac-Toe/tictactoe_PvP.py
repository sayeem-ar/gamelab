import pygame, sys

pygame.init()   # always need to initialize pygame if we use import pygame

# const
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

# colors
RED = (255, 0, 0)
BG_COLOR = (102, 178, 255)
LINE_COLOR = (96, 96, 96)     # (23, 135, 135)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe (PvP)')

# Load and set the window icon
icon = pygame.image.load(r'C:\Users\DarkBoyAR\Desktop\GitHub-sayeem-ar\gamelab\Tic-Tac-Toe\icon.png')  # Replace 'icon.png' with desired icon file
pygame.display.set_icon(icon)

screen.fill(BG_COLOR)

# Function to draw the lines of the Tic Tac Toe grid
def draw_lines():
    # horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

draw_lines()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
