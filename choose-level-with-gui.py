import tkinter as tk
import random

# Difficulty levels
DIFFICULTY = "medium"  # Change to "easy", "medium", or "hard"

mistake_chance = {
    "easy": 0.8,  # 80% mistakes
    "medium": 0.3,  # 30% mistakes
    "hard": 0.0  # Perfect AI
}

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        """Creates the game board with buttons."""
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(self.window, text=" ", font=("Arial", 24), height=2, width=5,
                                               command=lambda row=r, col=c: self.make_move(row, col))
                self.buttons[r][c].grid(row=r, column=c)

        self.label = tk.Label(self.window, text="Player X's Turn", font=("Arial", 16))
        self.label.grid(row=3, column=0, columnspan=3)

        # ADD A RESTART BUTTON
        self.restart_button = tk.Button(self.window, text="Restart Game", font=("Arial", 14), command=self.reset_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

    def reset_game(self):
        """Resets the board to start a new game."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.label.config(text="Player X's Turn")

        # Reset all buttons
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=" ", state=tk.NORMAL)

    def make_move(self, row, col):
        """Handles a player's move and AI's response."""
        if self.board[row][col] == " ":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state=tk.DISABLED)
            if self.check_winner("X"):
                self.label.config(text="Player X Wins!")
                self.end_game()
                return
            if self.is_full():
                self.label.config(text="It's a Draw!")
                self.end_game()
                return

            self.label.config(text="Computer's Turn")
            self.window.after(500, self.computer_move)

    def computer_move(self):
        """AI selects a move with a chance of making a mistake."""
        row, col = self.choose_ai_move()
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O", state=tk.DISABLED)

        if self.check_winner("O"):
            self.label.config(text="Computer Wins!")
            self.end_game()
            return
        if self.is_full():
            self.label.config(text="It's a Draw!")
            self.end_game()
            return

        self.label.config(text="Player X's Turn")

    def choose_ai_move(self):
        """Chooses a move using AI logic and difficulty settings."""
        if random.random() < mistake_chance[DIFFICULTY]:
            return self.make_mistake()
        else:
            return self.find_best_move()

    def make_mistake(self):
        """Makes a mistake by selecting a suboptimal move."""
        available_moves = self.get_available_moves()
        for row, col in available_moves:
            self.board[row][col] = "X"
            if self.check_winner("X"):
                self.board[row][col] = " "
                return row, col
            self.board[row][col] = " "
        if (1, 1) in available_moves:
            return (1, 1)
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        corner_moves = [move for move in corners if move in available_moves]
        if corner_moves:
            return random.choice(corner_moves)
        return random.choice(available_moves)

    def find_best_move(self):
        """Finds the best move using Minimax for an unbeatable AI."""
        best_score = -float("inf")
        best_move = None
        for row, col in self.get_available_moves():
            self.board[row][col] = "O"
            score = self.minimax(0, False)
            self.board[row][col] = " "
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move

    def minimax(self, depth, is_maximizing):
        """Minimax algorithm for perfect AI."""
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if self.is_full():
            return 0
        if is_maximizing:
            best_score = -float("inf")
            for row, col in self.get_available_moves():
                self.board[row][col] = "O"
                score = self.minimax(depth + 1, False)
                self.board[row][col] = " "
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for row, col in self.get_available_moves():
                self.board[row][col] = "X"
                score = self.minimax(depth + 1, True)
                self.board[row][col] = " "
                best_score = min(best_score, score)
            return best_score

    def check_winner(self, player):
        """Checks if a player has won."""
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        """Checks if the board is full."""
        return all(self.board[r][c] != " " for r in range(3) for c in range(3))

    def get_available_moves(self):
        """Returns available moves."""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]

    def end_game(self):
        """Disables buttons when the game ends."""
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(state=tk.DISABLED)

    def run(self):
        """Runs the game window."""
        self.window.mainloop()

# Start the game
game = TicTacToe()
game.run()