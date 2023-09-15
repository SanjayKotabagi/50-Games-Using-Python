import random

def create_crossword(rows, cols, words):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    placed_words = []

    def try_place(word):
        for _ in range(10):
            direction = random.choice(["horizontal", "vertical"])
            if direction == "horizontal":
                start_row = random.randint(0, rows - 1)
                start_col = random.randint(0, cols - len(word))
            else:
                start_row = random.randint(0, rows - len(word))
                start_col = random.randint(0, cols - 1)

            can_place = True
            for i in range(len(word)):
                if direction == "horizontal":
                    cell = grid[start_row][start_col + i]
                else:
                    cell = grid[start_row + i][start_col]

                if cell != ' ' and cell != word[i]:
                    can_place = False
                    break

            if can_place:
                if direction == "horizontal":
                    for i in range(len(word)):
                        grid[start_row][start_col + i] = word[i]
                else:
                    for i in range(len(word)):
                        grid[start_row + i][start_col] = word[i]
                placed_words.append((word, direction, start_row, start_col))
                return True
        return False

    for word in words:
        if not try_place(word):
            print(f"Failed to place word: {word}")

    return grid, placed_words

def print_crossword(grid):
    for row in grid:
        print(' '.join(row))

def main():
    rows, cols = 15, 15
    words = ["PYTHON", "PROGRAMMING", "CROSSWORD", "PUZZLE", "GRID", "WORD", "HORIZONTAL", "VERTICAL"]
    
    grid, placed_words = create_crossword(rows, cols, words)
    print("Crossword Puzzle:")
    print_crossword(grid)

if __name__ == "__main__":
    main()
