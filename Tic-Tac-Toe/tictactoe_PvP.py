import pygame, sys
import numpy as np

pygame.init()   # always need to initialize pygame if we use import pygame

# const
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3

# colors
RED = (255, 0, 0)
BG_COLOR = (102, 178, 255)
LINE_COLOR = (96, 96, 96)     # (23, 135, 135)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe (PvP)')

# Load and set the window icon
icon = pygame.image.load(r'F:\ar_sayeem_github\gamelab\Tic-Tac-Toe\icon.png')  # Replace 'path' with desired icon file location
pygame.display.set_icon(icon)

screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
#print(board)


# Function to draw the lines of the Tic Tac Toe grid
def draw_lines():
    # horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def avainable_square(row, col):
    return board[row][col] == 0       # [same as below comment]
''' if board[row][col]:
        return True
    else:
        return False
'''

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    
    return True

# false
print(is_board_full())

#marking all squares
for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            mark_square(row, col, 1)
# board is full true
print(is_board_full())




# is the middle square abailable?
# print(avainable_square(1, 1))
# mark_square(1, 1, 1)                # (1, 1) spot taken by P1, so not available
# print(avainable_square(1, 1))


# mark_square(0, 0, 1)
# mark_square(1, 1, 2)







# print(board)





draw_lines()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
