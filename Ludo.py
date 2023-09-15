import random

# Constants
BOARD_SIZE = 40
NUM_PLAYERS = 4
NUM_PIECES = 4

# Define the players' colors
PLAYER_COLORS = {
    0: "Red",
    1: "Blue",
    2: "Green",
    3: "Yellow",
}

# Define the Ludo board
board = [" " for _ in range(BOARD_SIZE)]

# Define the player positions and pieces
player_positions = [0] * NUM_PLAYERS
player_pieces = [[0] * NUM_PIECES for _ in range(NUM_PLAYERS)]

# Initialize the board with players' pieces
for player in range(NUM_PLAYERS):
    for piece in range(NUM_PIECES):
        board[player * 10 + piece] = str(player)
        player_pieces[player][piece] = player * 10 + piece

# Function to display the Ludo board
def display_board():
    print("Ludo Board:")
    for i, cell in enumerate(board):
        if i % 10 == 0:
            print()
        print(cell, end=" ")
    print("\n")

# Function to roll a die (1 to 6)
def roll_die():
    return random.randint(1, 6)

# Function to move a piece
def move_piece(player, piece, steps):
    current_position = player_pieces[player][piece]
    new_position = (current_position + steps) % BOARD_SIZE

    if board[new_position] == " " or board[new_position] == str(player):
        board[current_position] = " "
        player_pieces[player][piece] = new_position
        board[new_position] = str(player)
        return True

    return False

# Main game loop
current_player = 0
winner = None

while True:
    display_board()
    print(f"{PLAYER_COLORS[current_player]}'s turn")

    input("Press Enter to roll the die...")

    steps = roll_die()
    print(f"{PLAYER_COLORS[current_player]} rolled a {steps}")

    valid_move = False
    for piece in range(NUM_PIECES):
        if move_piece(current_player, piece, steps):
            valid_move = True
            break

    if not valid_move:
        print(f"No valid moves for {PLAYER_COLORS[current_player]}")

    if all(position == BOARD_SIZE - 1 for position in player_positions):
        winner = current_player
        break

    current_player = (current_player + 1) % NUM_PLAYERS

print(f"{PLAYER_COLORS[winner]} wins!")

