import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Function to draw the Sudoku grid
def draw_grid(board):
    for i in range(GRID_SIZE + 1):
        thickness = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)

# Function to draw the Sudoku board
def draw_board(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = board[row][col]
            if cell_value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(cell_value), True, BLACK)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

# Function to generate a new Sudoku puzzle
def generate_sudoku():
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    solve_sudoku(board)  # Generate a solved Sudoku puzzle
    remove_cells(board, random.randint(40, 50))  # Remove some cells to make it a puzzle
    return board

# Function to remove cells to create a puzzle
def remove_cells(board, num_cells):
    cells_to_remove = random.sample([(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE)], num_cells)
    for row, col in cells_to_remove:
        board[row][col] = 0

# Function to solve a Sudoku puzzle
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # No empty cells left, puzzle solved
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack if the solution is not found

    return False

# Function to check if a move is valid
def is_valid_move(board, row, col, num):
    for i in range(GRID_SIZE):
        if board[row][i] == num or board[i][col] == num:
            return False

    row_start, col_start = 3 * (row // 3), 3 * (col // 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False

    return True

# Function to find an empty cell
def find_empty_cell(board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                return i, j
    return None

# Main game loop
def main():
    sudoku_board = generate_sudoku()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(sudoku_board)
        draw_board(sudoku_board)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
