import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Create a grid for the maze
grid = [[1] * COLS for _ in range(ROWS)]

# Maze generation using recursive backtracking
def generate_maze(x, y):
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < COLS and 0 <= ny < ROWS and grid[ny][nx] == 1:
            grid[ny][nx] = 0
            grid[y + dy // 2][x + dx // 2] = 0
            generate_maze(nx, ny)

# Start generating the maze from the center
start_x, start_y = COLS // 2, ROWS // 2
grid[start_y][start_x] = 0
generate_maze(start_x, start_y)

# Game loop
running = True
player_x, player_y = 1, 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0 and grid[player_y - 1][player_x] == 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and player_y < ROWS - 1 and grid[player_y + 1][player_x] == 0:
        player_y += 1
    if keys[pygame.K_LEFT] and player_x > 0 and grid[player_y][player_x - 1] == 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and player_x < COLS - 1 and grid[player_y][player_x + 1] == 0:
        player_x += 1

    screen.fill(BLACK)
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, GREEN, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

pygame.quit()
