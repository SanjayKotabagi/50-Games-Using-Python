import pygame
import random

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [0, 1, 1]]
]

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Initialize font
font = pygame.font.Font(None, 36)

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Function to draw a shape
def draw_shape(shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (x + col * GRID_SIZE, y + row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Function to check if a shape can be placed in a certain position
def can_place(shape, grid, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == 1:
                if x + col < 0 or x + col >= GRID_WIDTH or y + row >= GRID_HEIGHT or grid[y + row][x + col] == 1:
                    return False
    return True

# Function to clear completed rows
def clear_rows(grid):
    full_rows = [i for i, row in enumerate(grid) if all(row)]
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)

# Main game loop
def main():
    clock = pygame.time.Clock()
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_shape = random.choice(SHAPES)
    x, y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and can_place(current_shape, grid, x - 1, y):
                    x -= 1
                elif event.key == pygame.K_RIGHT and can_place(current_shape, grid, x + 1, y):
                    x += 1
                elif event.key == pygame.K_DOWN and can_place(current_shape, grid, x, y + 1):
                    y += 1

        if can_place(current_shape, grid, x, y + 1):
            y += 1
        else:
            for row in range(len(current_shape)):
                for col in range(len(current_shape[row])):
                    if current_shape[row][col] == 1:
                        grid[y + row][x + col] = 1
            clear_rows(grid)
            current_shape = random.choice(SHAPES)
            x, y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

        screen.fill(BLACK)
        draw_grid()
        draw_shape(current_shape, x * GRID_SIZE, y * GRID_SIZE)

        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if grid[row][col] == 1:
                    pygame.draw.rect(screen, WHITE, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        clock.tick(5)  # Adjust this value for the game's speed

if __name__ == "__main__":
    main()
