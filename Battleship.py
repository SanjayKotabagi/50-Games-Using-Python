import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (192, 192, 192)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Initialize game variables
player_board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
enemy_board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
enemy_ship_row = random.randint(0, GRID_SIZE - 1)
enemy_ship_col = random.randint(0, GRID_SIZE - 1)
player_hits = 0
max_hits = 3

# Initialize fonts
font = pygame.font.Font(None, 36)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def draw_board(board, offset_x, offset_y):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_x = offset_x + col * CELL_SIZE
            cell_y = offset_y + row * CELL_SIZE
            pygame.draw.rect(screen, WHITE, (cell_x, cell_y, CELL_SIZE, CELL_SIZE), 2)
            text = font.render(board[row][col], True, WHITE)
            text_rect = text.get_rect(center=(cell_x + CELL_SIZE // 2, cell_y + CELL_SIZE // 2))
            screen.blit(text, text_rect)

def check_hit(row, col):
    global player_hits
    if row == enemy_ship_row and col == enemy_ship_col:
        player_hits += 1
        return True
    return False

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and player_hits < max_hits:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if enemy_board[row][col] == ' ':
                    if check_hit(row, col):
                        enemy_board[row][col] = 'X'
                    else:
                        enemy_board[row][col] = 'O'

        screen.fill(BLUE)
        draw_grid()
        draw_board(player_board, 0, 0)
        draw_board(enemy_board, WIDTH // 2, 0)

        if player_hits == max_hits:
            font = pygame.font.Font(None, 72)
            win_text = font.render("You win!", True, WHITE)
            screen.blit(win_text, (WIDTH // 4, HEIGHT // 2 - 36))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
