import pygame
import random

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Snake starting position and direction
snake_x, snake_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
snake_dx, snake_dy = 0, 0

# Snake body
snake_body = [(snake_x, snake_y)]

# Food position
food_x, food_y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

# Score
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy == 0:
                snake_dx, snake_dy = 0, -1
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx, snake_dy = 0, 1
            elif event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx, snake_dy = -1, 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx, snake_dy = 1, 0

    # Update snake's position
    new_head = (snake_body[0][0] + snake_dx, snake_body[0][1] + snake_dy)
    snake_body.insert(0, new_head)

    # Check for collisions with food
    if snake_body[0] == (food_x, food_y):
        score += 1
        food_x, food_y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
    else:
        snake_body.pop()

    # Check for collisions with walls or itself
    if (
        snake_body[0][0] < 0 or snake_body[0][0] >= GRID_WIDTH or
        snake_body[0][1] < 0 or snake_body[0][1] >= GRID_HEIGHT or
        snake_body[0] in snake_body[1:]
    ):
        running = False

    # Draw everything
    screen.fill(WHITE)

    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, RED, (food_x * GRID_SIZE, food_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(SNAKE_SPEED)

# Game over
pygame.quit()
