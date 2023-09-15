class ChessGame:
    def __init__(self):
        self.board = self.setup_board()
        self.current_player = "White"
        self.game_over = False

    def setup_board(self):
        board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        return board

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print("\n")

    def is_valid_move(self, start, end):
        # Check if the move is within the board boundaries
        if not (0 <= start[0] < 8) or not (0 <= start[1] < 8) or not (0 <= end[0] < 8) or not (0 <= end[1] < 8):
            return False

        piece = self.board[start[0]][start[1]]
        target = self.board[end[0]][end[1]]

        # Check if the piece belongs to the current player
        if self.current_player == "White" and piece[0] != "w":
            return False
        elif self.current_player == "Black" and piece[0] != "b":
            return False

        # Check if the target square is empty or contains an opponent's piece
        if target == "  " or (self.current_player == "White" and target[0] == "b") or (self.current_player == "Black" and target[0] == "w"):
            return True

        return False

    def move_piece(self, start, end):
        if self.is_valid_move(start, end):
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = "  "
            return True
        return False

    def play_game(self):
        while not self.game_over:
            self.print_board()
            print(f"{self.current_player}'s turn.")

            start = input("Enter the start position (e.g., 'a2'): ").strip().lower()
            end = input("Enter the end position: ").strip().lower()

            start_col, start_row = ord(start[0]) - ord("a"), int(start[1]) - 1
            end_col, end_row = ord(end[0]) - ord("a"), int(end[1]) - 1

            if self.move_piece((start_row, start_col), (end_row, end_col)):
                self.current_player = "Black" if self.current_player == "White" else "White"
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.play_game()
