import random
import copy

# Initialize the game board
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Add a new tile (either 2 or 4) to a random empty cell
def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

# Print the game board
def print_board(board):
    for row in board:
        print(" ".join(str(tile) if tile != 0 else "." for tile in row))
    print()

# Move tiles to the left
def move_left(board):
    new_board = copy.deepcopy(board)
    for row in new_board:
        row.sort(key=lambda x: 0 if x == 0 else 1)
        for j in range(3):
            if row[j] == row[j + 1]:
                row[j] *= 2
                row[j + 1] = 0
        row.sort(key=lambda x: 0 if x == 0 else 1)
    return new_board

# Rotate the board 90 degrees counter-clockwise
def rotate_board(board):
    return [[board[j][i] for j in range(4)] for i in range(3, -1, -1)]

# Check if the game is over (no more legal moves)
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True

# Display game instructions
def display_instructions():
    print("Welcome to 2048!")
    print("Use W/A/S/D to move tiles Up/Left/Down/Right.")
    print("Combine identical tiles to reach 2048!")
    print("Enjoy the game!\n")

# Main game loop
def main():
    display_instructions()
    board = initialize_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("Game Over!")
            break
        direction = input("Enter move (W/A/S/D): ").upper()
        if direction not in ["W", "A", "S", "D"]:
            print("Invalid input! Use W/A/S/D.")
            continue
        if direction == "A":
            board = move_left(board)
        elif direction == "W":
            board = rotate_board(board)
            board = move_left(board)
            board = rotate_board(board)
            board = rotate_board(board)
            board = rotate_board(board)
        elif direction == "S":
            board = rotate_board(board)
            board = rotate_board(board)
            board = rotate_board(board)
            board = move_left(board)
            board = rotate_board(board)
        elif direction == "D":
            board = rotate_board(board)
            board = rotate_board(board)
            board = move_left(board)
            board = rotate_board(board)
            board = rotate_board(board)
        add_new_tile(board)

if __name__ == "__main__":
    main()
