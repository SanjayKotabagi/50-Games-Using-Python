import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
MOLE_RADIUS = 25
MOLE_SPEED = 3
MOLE_APPEAR_DELAY = 1000  # milliseconds
WHITE = (255, 255, 255)
MOLE_COLOR = (255, 0, 0)  # Red color for the mole

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Initialize game variables
moles = []
score = 0
font = pygame.font.Font(None, 36)

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def create_mole():
    x = random.randint(MOLE_RADIUS, WIDTH - MOLE_RADIUS)
    y = random.randint(MOLE_RADIUS, HEIGHT - MOLE_RADIUS)
    moles.append([x, y])

def main():
    global score  # Declare score as a global variable

    last_mole_appear_time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for mole in moles:
                    if pygame.Rect(mole[0] - MOLE_RADIUS, mole[1] - MOLE_RADIUS, 2 * MOLE_RADIUS, 2 * MOLE_RADIUS).collidepoint(event.pos):
                        moles.remove(mole)
                        score += 1

        current_time = pygame.time.get_ticks()

        if current_time - last_mole_appear_time > MOLE_APPEAR_DELAY:
            create_mole()
            last_mole_appear_time = current_time

        screen.fill((0, 0, 0))

        for mole in moles:
            mole[1] += MOLE_SPEED
            pygame.draw.circle(screen, MOLE_COLOR, (mole[0], mole[1]), MOLE_RADIUS)

        draw_score()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
