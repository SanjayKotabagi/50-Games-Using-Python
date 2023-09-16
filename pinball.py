import pygame
import random

# Constants
WIDTH, HEIGHT = 400, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_SPEED = 5
PADDLE_SPEED = 8
WALL_COLOR = (255, 255, 255)
BALL_COLOR = (255, 0, 0)
PADDLE_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball")

# Initialize font
font = pygame.font.Font(None, 36)

# Create the ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Define ball speed as global variables
ball_speed_x = random.choice((1, -1)) * BALL_SPEED
ball_speed_y = -BALL_SPEED

# Create the paddles
left_paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Main game loop
def main():
    global ball_speed_x, ball_speed_y  # Declare these variables as global
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and left_paddle.left > 0:
            left_paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and left_paddle.right < WIDTH:
            left_paddle.x += PADDLE_SPEED

        if keys[pygame.K_a] and right_paddle.left > 0:
            right_paddle.x -= PADDLE_SPEED
        if keys[pygame.K_d] and right_paddle.right < WIDTH:
            right_paddle.x += PADDLE_SPEED

        # Update ball position
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with walls
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x *= -1

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_y *= -1

        # Ball out of bounds (game over)
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            game_over = True

        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, WALL_COLOR, left_paddle)
        pygame.draw.rect(screen, WALL_COLOR, right_paddle)
        pygame.draw.ellipse(screen, BALL_COLOR, ball)

        pygame.display.flip()
        clock.tick(FPS)

    game_over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()

if __name__ == "__main__":
    main()
