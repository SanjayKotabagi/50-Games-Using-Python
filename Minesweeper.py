import tkinter as tk
import random

class Minesweeper:
    def __init__(self, root, rows, cols, num_mines):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.is_mine = [[False for _ in range(cols)] for _ in range(rows)]
        self.uncovered = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False

        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        self.reset_button = tk.Button(self.root, text="New Game", command=self.reset_game)
        self.reset_button.pack()

        self.canvas = tk.Canvas(self.root, width=self.cols * 30, height=self.rows * 30)
        self.canvas.pack()

        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self.canvas, width=2, height=1, command=lambda r=row, c=col: self.click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def place_mines(self):
        for _ in range(self.num_mines):
            while True:
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.cols - 1)
                if not self.is_mine[row][col]:
                    self.is_mine[row][col] = True
                    break

    def calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_mine[row][col]:
                    continue
                mines_around = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.is_mine[nr][nc]:
                            mines_around += 1
                self.board[row][col] = mines_around

    def reveal_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_mine[row][col]:
                    self.buttons[row][col].config(text="*", state=tk.DISABLED)

    def uncover(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.uncovered[row][col]:
            return
        self.uncovered[row][col] = True
        self.buttons[row][col].config(state=tk.DISABLED, text=str(self.board[row][col]), relief=tk.SUNKEN)

        if self.board[row][col] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    self.uncover(row + dr, col + dc)

    def click(self, row, col):
        if self.game_over or self.uncovered[row][col]:
            return

        if self.is_mine[row][col]:
            self.game_over = True
            self.buttons[row][col].config(text="*", state=tk.DISABLED, bg="red")
            self.reveal_mines()
            self.reset_button.config(text="Game Over")
        else:
            self.uncover(row, col)
            self.check_win()

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.is_mine[row][col] and not self.uncovered[row][col]:
                    return
        self.game_over = True
        self.reset_button.config(text="You Win!")

    def reset_game(self):
        self.game_over = False
        self.reset_button.config(text="New Game")
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.root, width=self.cols * 30, height=self.rows * 30)
        self.canvas.pack()
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.is_mine = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.uncovered = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, rows=10, cols=10, num_mines=20)
    root.mainloop()
