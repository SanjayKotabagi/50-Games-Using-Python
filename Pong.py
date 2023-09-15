import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 400
BALL_SPEED = 5
PADDLE_SPEED = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10
WHITE = (255, 255, 255)
FPS = 60

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Initialize clock
clock = pygame.time.Clock()

# Paddle positions
left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2
right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice((1, -1)) * BALL_SPEED
ball_dy = random.choice((1, -1)) * BALL_SPEED

# Score
left_score = 0
right_score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_dy *= -1

    # Ball collision with paddles
    if (ball_x <= PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT) or (
            ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT):
        ball_dx *= -1

    # Ball out of bounds
    if ball_x < 0:
        right_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = random.choice((1, -1)) * BALL_SPEED
        ball_dy = random.choice((1, -1)) * BALL_SPEED
    elif ball_x > WIDTH:
        left_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = random.choice((1, -1)) * BALL_SPEED
        ball_dy = random.choice((1, -1)) * BALL_SPEED

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Display scores
    font = pygame.font.Font(None, 36)
    left_text = font.render(f"Left: {left_score}", True, WHITE)
    right_text = font.render(f"Right: {right_score}", True, WHITE)
    screen.blit(left_text, (50, 10))
    screen.blit(right_text, (WIDTH - 200, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
