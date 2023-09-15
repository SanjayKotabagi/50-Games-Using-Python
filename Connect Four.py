import pygame
import sys

# Constants
ROWS = 6
COLS = 7
CELL_SIZE = 100
WIDTH = COLS * CELL_SIZE
HEIGHT = (ROWS + 1) * CELL_SIZE
PLAYER1_COLOR = (255, 0, 0)
PLAYER2_COLOR = (0, 0, 255)
EMPTY_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
PLAYER1 = "X"
PLAYER2 = "O"
EMPTY = " "
FONT_SIZE = 36
WIN_TEXT = "WIN!"
DRAW_TEXT = "DRAW!"

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

# Function to create an empty game board
def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

# Function to draw the game board
def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, EMPTY_COLOR, (col * CELL_SIZE, (row + 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if board[row][col] == PLAYER1:
                pygame.draw.circle(screen, PLAYER1_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)
            elif board[row][col] == PLAYER2:
                pygame.draw.circle(screen, PLAYER2_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

# Function to check if a column is full
def is_column_full(board, col):
    return board[0][col] != EMPTY

# Function to drop a piece in a column
def drop_piece(board, col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return True
    return False

# Function to check if a player has won
def check_win(board, piece):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    return False

# Main game loop
def main():
    board = create_board()
    current_player = PLAYER1
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, EMPTY_COLOR, (0, 0, WIDTH, CELL_SIZE))
                pos_x = event.pos[0]
                pygame.draw.circle(screen, PLAYER1_COLOR if current_player == PLAYER1 else PLAYER2_COLOR, (pos_x, CELL_SIZE // 2), CELL_SIZE // 2 - 5)
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // CELL_SIZE
                if is_column_full(board, col):
                    continue
                if not drop_piece(board, col, current_player):
                    continue

                if check_win(board, current_player):
                    draw_board(board)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    pygame.font.init()
                    font = pygame.font.SysFont(None, FONT_SIZE)
                    text = font.render(f"Player {current_player} {WIN_TEXT}", True, PLAYER1_COLOR if current_player == PLAYER1 else PLAYER2_COLOR)
                    screen.blit(text, (WIDTH // 4, CELL_SIZE // 4))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    game_over = True
                elif all(board[0][i] != EMPTY for i in range(COLS)):
                    draw_board(board)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    pygame.font.init()
                    font = pygame.font.SysFont(None, FONT_SIZE)
                    text = font.render(f"{DRAW_TEXT}", True, LINE_COLOR)
                    screen.blit(text, (WIDTH // 3, CELL_SIZE // 4))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    game_over = True
                else:
                    current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1

        draw_board(board)
        pygame.display.update()

if __name__ == "__main__":
    main()
