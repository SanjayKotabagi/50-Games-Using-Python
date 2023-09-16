import random

# Initialize the board
board_size = 15
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

# Initialize the bag of letter tiles
letter_tiles = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

# Function to draw random tiles for a player
def draw_tiles(player_tiles, num_tiles):
    tiles = []
    for _ in range(num_tiles):
        tile = random.choice(list(player_tiles.keys()))
        player_tiles[tile] -= 1
        if player_tiles[tile] == 0:
            del player_tiles[tile]
        tiles.append(tile)
    return tiles

# Function to display the board
def display_board(board):
    for row in board:
        print(' '.join(row))

# Function to place a word on the board
def place_word(board, word, row, col, direction):
    if direction == 'across':
        for letter in word:
            board[row][col] = letter
            col += 1
    elif direction == 'down':
        for letter in word:
            board[row][col] = letter
            row += 1

# Function to check if a word is valid
def is_valid_word(word):
    # Replace with a real dictionary check if needed
    return True

# Main game loop
player1_tiles = draw_tiles(letter_tiles, 7)
player2_tiles = draw_tiles(letter_tiles, 7)
players = [player1_tiles, player2_tiles]
current_player = 0

while True:
    display_board(board)
    print(f"Player {current_player + 1}'s Turn")
    print(f"Your Tiles: {' '.join(players[current_player])}")

    row = int(input("Enter the row (0-14): "))
    col = int(input("Enter the column (0-14): "))
    direction = input("Enter direction (across/down): ").lower()
    word = input("Enter your word: ").upper()

    if is_valid_word(word):
        place_word(board, word, row, col, direction)
        for letter in word:
            players[current_player].append(letter)
        current_player = 1 - current_player
    else:
        print("Invalid word. Try again.")

# This simplified example allows two players to take turns forming words on a 15x15 board using randomly assigned letter tiles. The game loop continues indefinitely until you choose to exit. It is a starting point, and you can expand and improve upon it to create a more feature-rich Scrabble-like game.
