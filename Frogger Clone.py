import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 50
FROG_SIZE = 40
FROG_SPEED = 50
OBSTACLE_SPEED = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Initialize game variables
frog_x = WIDTH // 2 - FROG_SIZE // 2
frog_y = HEIGHT - GRID_SIZE - FROG_SIZE
obstacle_x = random.randint(0, WIDTH - GRID_SIZE)
obstacle_y = random.randint(GRID_SIZE, HEIGHT - GRID_SIZE)
game_over = False

def draw_frog(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, FROG_SIZE, FROG_SIZE))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, GRID_SIZE, GRID_SIZE))

def check_collision():
    global frog_x, frog_y, obstacle_x, obstacle_y
    if (
        frog_x + FROG_SIZE >= obstacle_x
        and frog_x <= obstacle_x + GRID_SIZE
        and frog_y + FROG_SIZE >= obstacle_y
        and frog_y <= obstacle_y + GRID_SIZE
    ):
        return True
    return False

def main():
    global frog_x, frog_y, game_over, obstacle_x, obstacle_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and frog_y > 0:
                        frog_y -= FROG_SPEED
                    elif event.key == pygame.K_DOWN and frog_y < HEIGHT - GRID_SIZE - FROG_SIZE:
                        frog_y += FROG_SPEED
                    elif event.key == pygame.K_LEFT and frog_x > 0:
                        frog_x -= FROG_SPEED
                    elif event.key == pygame.K_RIGHT and frog_x < WIDTH - FROG_SIZE:
                        frog_x += FROG_SPEED

        if not game_over:
            obstacle_x -= OBSTACLE_SPEED
            if obstacle_x < -GRID_SIZE:
                obstacle_x = WIDTH
                obstacle_y = random.randint(GRID_SIZE, HEIGHT - GRID_SIZE)

            if check_collision():
                game_over = True

        screen.fill((0, 0, 0))

        if not game_over:
            draw_frog(frog_x, frog_y)
            draw_obstacle(obstacle_x, obstacle_y)
        else:
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("Game Over", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 36))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
