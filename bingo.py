import random

class BingoGame:
    def __init__(self):
        self.board = self.generate_board()
        self.called_numbers = []
        self.is_winner = False

    def generate_board(self):
        board = []
        for _ in range(5):
            row = random.sample(range(1, 16), 5)
            row[2] = 0  # Center cell is free
            board.append(row)
        return board

    def print_board(self):
        print("\nBingo Board:")
        for row in self.board:
            row_str = " | ".join(map(str, row))
            print(row_str)
            print("-" * len(row_str))
        print("\n")

    def call_number(self):
        while True:
            called_number = random.randint(1, 75)
            if called_number not in self.called_numbers:
                self.called_numbers.append(called_number)
                return called_number

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(5):
            if all(self.board[i][j] == 0 for j in range(5)):
                self.is_winner = True
                return True
            if all(self.board[j][i] == 0 for j in range(5)):
                self.is_winner = True
                return True
        if all(self.board[i][i] == 0 for i in range(5)) or all(self.board[i][4 - i] == 0 for i in range(5)):
            self.is_winner = True
            return True
        return False

    def play_game(self):
        print("Welcome to Bingo!")
        self.print_board()

        while not self.is_winner:
            input("Press Enter to call a number...")
            called_number = self.call_number()
            print(f"Called number: {called_number}")

            for i in range(5):
                for j in range(5):
                    if self.board[i][j] == called_number:
                        self.board[i][j] = 0

            self.print_board()

            if self.check_winner():
                print("Bingo! You are the winner!")

if __name__ == "__main__":
    bingo_game = BingoGame()
    bingo_game.play_game()
