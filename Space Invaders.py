import pygame
import random

# Constants
WIDTH, HEIGHT = 400, 400
PLAYER_SIZE = 30
PLAYER_SPEED = 5
ENEMY_SIZE = 20
ENEMY_SPEED = 2
BULLET_SIZE = 5
BULLET_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Initialize font
font = pygame.font.Font(None, 36)

# Create the player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Create enemies
enemies = []
for _ in range(5):
    enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(0, HEIGHT // 2), ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)

# Create bullets
bullets = []

# Function to move and draw the player
def move_player(direction):
    if direction == "left":
        player.x -= PLAYER_SPEED
    elif direction == "right":
        player.x += PLAYER_SPEED

def draw_player():
    pygame.draw.rect(screen, WHITE, player)

# Function to move and draw the enemies
def move_enemies():
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, enemy)

# Function to move and draw the bullets
def move_bullets():
    for bullet in bullets:
        bullet.y -= BULLET_SPEED

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

# Main game loop
def main():
    clock = pygame.time.Clock()
    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_player("left")
                elif event.key == pygame.K_RIGHT:
                    move_player("right")
                elif event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player.y, BULLET_SIZE, BULLET_SIZE)
                    bullets.append(bullet)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move_player("left")
        if keys[pygame.K_RIGHT]:
            move_player("right")

        move_enemies()
        move_bullets()

        # Check for collisions between bullets and enemies
        for bullet in bullets:
            for enemy in enemies:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10

        # Check for game over condition
        for enemy in enemies:
            if enemy.colliderect(player):
                game_over = True

        screen.fill(BLACK)

        draw_player()
        draw_enemies()
        draw_bullets()

        # Display the score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # Game over screen
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
    pygame.display.flip()
    pygame.time.delay(2000)  # Display the game over screen for 2 seconds

if __name__ == "__main__":
    main()
