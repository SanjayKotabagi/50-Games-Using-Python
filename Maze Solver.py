#pip install pygame

#install above library to play game.

import pygame
import random

# Constants for colors and dimensions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")

# Maze dimensions
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Create a grid
grid = [[0] * COLS for _ in range(ROWS)]

# Generate a random maze using recursive backtracking algorithm
def generate_maze(x, y):
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < COLS and 0 <= new_y < ROWS and grid[new_y][new_x] == 0:
            grid[new_y][new_x] = 1  # Mark the cell as visited
            grid[y + dy // 2][x + dx // 2] = 1  # Mark the wall as visited
            generate_maze(new_x, new_y)

# Solve the maze using Depth-First Search (DFS)
def solve_maze(x, y):
    if x < 0 or x >= COLS or y < 0 or y >= ROWS or grid[y][x] != 1:
        return False

    grid[y][x] = 2  # Mark the cell as part of the solution path

    if x == COLS - 1 and y == ROWS - 1:
        return True  # Reached the exit

    if solve_maze(x + 1, y) or solve_maze(x - 1, y) or solve_maze(x, y + 1) or solve_maze(x, y - 1):
        return True

    grid[y][x] = 3  # Mark the cell as part of a failed path
    return False

# Generate the maze and solve it
generate_maze(1, 1)
solve_maze(1, 1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze
    screen.fill(WHITE)
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] == 0:  # Wall
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[y][x] == 2:  # Solution path
                pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[y][x] == 3:  # Failed path
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

pygame.quit()
