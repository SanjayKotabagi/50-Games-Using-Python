import pygame
import random
import time

# Constants
WIDTH, HEIGHT = 300, 400
PLATFORM_WIDTH = 60
PLATFORM_HEIGHT = 10
PLAYER_SIZE = 20
PLAYER_JUMP = -13
GRAVITY = 0.9  # Increased gravity for more realistic jumping
PLATFORM_COLOR = (0, 255, 0)
PLAYER_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

# Initialize font
font = pygame.font.Font(None, 36)

# Create the player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT // 2 - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE)
player_velocity = 0

# Create platforms
platforms = []
for i in range(10):
    platform = pygame.Rect(random.randint(0, WIDTH - PLATFORM_WIDTH), i * (HEIGHT // 10), PLATFORM_WIDTH, PLATFORM_HEIGHT)
    platforms.append(platform)

# Function to display countdown
def display_countdown(count):
    countdown_text = font.render(str(count), True, (255, 255, 255))
    screen.blit(countdown_text, (WIDTH // 2 - 20, HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.delay(1000)  # Delay for 1 second

# Function to start the game countdown
def start_countdown():
    for i in range(3, 0, -1):
        screen.fill(BACKGROUND_COLOR)
        display_countdown(i)

# Main game loop
def main():
    global player_velocity
    clock = pygame.time.Clock()
    score = 0
    game_over = False
    game_started = False

    start_countdown()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        
        if not game_started:
            player_velocity = PLAYER_JUMP
            game_started = True

        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5

        player_velocity += GRAVITY
        player.y += player_velocity

        if player.y >= HEIGHT:
            game_over = True

        if player_velocity > 0:  # Only check for collision when falling
            for platform in platforms:
                if player.colliderect(platform) and player.bottom <= platform.centery:
                    player_velocity = PLAYER_JUMP
                    score += 1

        # Scroll the platforms when the player is near the top of the screen
        if player.top <= HEIGHT // 4:
            for platform in platforms:
                platform.y += abs(player_velocity)
                if platform.top >= HEIGHT:
                    platform.top = -PLATFORM_HEIGHT
                    platform.left = random.randint(0, WIDTH - PLATFORM_WIDTH)

        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, PLAYER_COLOR, player)
        for platform in platforms:
            pygame.draw.rect(screen, PLATFORM_COLOR, platform)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    game_over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()

if __name__ == "__main__":
    main()
