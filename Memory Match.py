import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 4
CARD_SIZE = 100
GAP = 10
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
FPS = 60

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Match Game")

# Initialize clock
clock = pygame.time.Clock()

# Create cards with matching pairs
card_values = [i for i in range(GRID_SIZE * GRID_SIZE)] * 2
random.shuffle(card_values)
revealed = [False] * (GRID_SIZE * GRID_SIZE)

# Position of cards
card_positions = []
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        x = col * (CARD_SIZE + GAP) + (WIDTH - GRID_SIZE * (CARD_SIZE + GAP)) // 2
        y = row * (CARD_SIZE + GAP) + (HEIGHT - GRID_SIZE * (CARD_SIZE + GAP)) // 2
        card_positions.append((x, y))

# Initialize game variables
selected_card1 = None
selected_card2 = None
matched_pairs = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and matched_pairs < GRID_SIZE * GRID_SIZE // 2:
            clicked_card = None
            for i, (x, y) in enumerate(card_positions):
                if not revealed[i] and x < event.pos[0] < x + CARD_SIZE and y < event.pos[1] < y + CARD_SIZE:
                    clicked_card = i
                    break

            if clicked_card is not None:
                if selected_card1 is None:
                    selected_card1 = clicked_card
                    revealed[selected_card1] = True
                elif selected_card2 is None and selected_card1 != clicked_card:
                    selected_card2 = clicked_card
                    revealed[selected_card2] = True

    # Check if two cards are revealed
    if selected_card1 is not None and selected_card2 is not None:
        pygame.time.wait(500)  # Delay for half a second to display the cards
        if card_values[selected_card1] == card_values[selected_card2]:
            matched_pairs += 1
        else:
            revealed[selected_card1] = revealed[selected_card2] = False
        selected_card1 = selected_card2 = None

    # Clear the screen
    screen.fill(WHITE)

    # Draw cards with numbered faces
    font = pygame.font.Font(None, 36)
    for i, (x, y) in enumerate(card_positions):
        if revealed[i]:
            pygame.draw.rect(screen, GRAY, (x, y, CARD_SIZE, CARD_SIZE))
            text = font.render(str(card_values[i]), True, WHITE)
            text_rect = text.get_rect(center=(x + CARD_SIZE / 2, y + CARD_SIZE / 2))
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, GRAY, (x, y, CARD_SIZE, CARD_SIZE))

    # Display matched pairs
    font = pygame.font.Font(None, 36)
    text = font.render(f"Matched Pairs: {matched_pairs}", True, GRAY)
    screen.blit(text, (20, 20))

    # Check for game over
    if matched_pairs == GRID_SIZE * GRID_SIZE // 2:
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over!", True, GRAY)
        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, (HEIGHT - game_over_text.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before closing the game
        running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
