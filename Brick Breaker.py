import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BALL_COLOR = (255, 0, 0)
PADDLE_COLOR = (0, 0, 255)
BRICK_COLOR = (0, 255, 0)
BRICK_WIDTH = 80
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLUMNS = 8
BRICK_SPACING = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BALL_SPEED = 5
PADDLE_SPEED = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Initialize game variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-1, 1]) * BALL_SPEED
ball_dy = -BALL_SPEED
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10
bricks = []

# Create bricks
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLUMNS):
        brick_x = col * (BRICK_WIDTH + BRICK_SPACING)
        brick_y = row * (BRICK_HEIGHT + BRICK_SPACING) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

def main():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_x, paddle_y  # Declare as global

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
            paddle_x += PADDLE_SPEED

        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with walls
        if ball_x < 0 or ball_x > WIDTH:
            ball_dx *= -1
        if ball_y < 0:
            ball_dy *= -1

        # Ball collision with paddle
        if (
            ball_y + BALL_RADIUS >= paddle_y
            and ball_x + BALL_RADIUS >= paddle_x
            and ball_x - BALL_RADIUS <= paddle_x + PADDLE_WIDTH
        ):
            ball_dy *= -1

        # Ball collision with bricks
        for brick in bricks:
            if (
                ball_x + BALL_RADIUS >= brick.left
                and ball_x - BALL_RADIUS <= brick.right
                and ball_y + BALL_RADIUS >= brick.top
                and ball_y - BALL_RADIUS <= brick.bottom
            ):
                bricks.remove(brick)
                ball_dy *= -1

        screen.fill(WHITE)
        pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
        pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        draw_bricks()

        if len(bricks) == 0:
            font = pygame.font.Font(None, 36)
            win_text = font.render("You win!", True, (0, 0, 0))
            screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2 - 18))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
