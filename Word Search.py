import random

# List of words to hide in the puzzle
words_to_find = ["PYTHON", "PROGRAMMING", "ALGORITHM", "PUZZLE", "SEARCH", "WORD"]

# Dimensions of the word search grid
rows = 10
cols = 10

# Initialize the grid with random letters
grid = [['' for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Place words horizontally or vertically
for word in words_to_find:
    direction = random.choice(["horizontal", "vertical"])
    if direction == "horizontal":
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - len(word))
        for i in range(len(word)):
            grid[row][col + i] = word[i]
    else:
        row = random.randint(0, rows - len(word))
        col = random.randint(0, cols - 1)
        for i in range(len(word)):
            grid[row + i][col] = word[i]

# Print the word search puzzle
for row in grid:
    print(' '.join(row))

# Create a function to check if a word is found in the grid
def find_word(word, grid):
    word_length = len(word)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col + word_length <= len(grid[row]) and ''.join(grid[row][col:col+word_length]) == word:
                return (row, col, row, col+word_length-1)
            if row + word_length <= len(grid) and ''.join(grid[row:row+word_length][col]) == word:
                return (row, col, row+word_length-1, col)
    return None

# Main game loop
found_words = []
while True:
    print("\nFound words:", ', '.join(found_words))
    word_to_find = input("Enter a word to find (or 'q' to quit): ").upper()
    if word_to_find == 'Q':
        break
    if word_to_find in found_words:
        print("You've already found this word.")
        continue
    result = find_word(word_to_find, grid)
    if result:
        found_words.append(word_to_find)
        print(f"Found '{word_to_find}' at ({result[0]},{result[1]}) to ({result[2]},{result[3]})!")
    else:
        print(f"Word '{word_to_find}' not found in the puzzle.")

print("Thanks for playing!")
