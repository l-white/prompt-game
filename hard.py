import random

def print_board(board):
    """Prints the Tic-Tac-Toe board in a readable format."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if a player has won the game."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_available_moves(board):
    """Finds all empty spaces on the board."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def find_best_move(board, computer, player):
    """AI logic to find the best move: win, block, center, corner, side."""
    available_moves = get_available_moves(board)

    # 1️⃣ Check if the computer can win
    for row, col in available_moves:
        board[row][col] = computer
        if check_winner(board, computer):
            return row, col  # Win immediately
        board[row][col] = " "  # Undo move

    # 2️⃣ Check if the player can win next turn (block them)
    for row, col in available_moves:
        board[row][col] = player
        if check_winner(board, player):
            return row, col  # Block player's win
        board[row][col] = " "  # Undo move

    # 3️⃣ Take the center if available
    if (1, 1) in available_moves:
        return (1, 1)

    # 4️⃣ Take a corner if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    corner_moves = [move for move in corners if move in available_moves]
    if corner_moves:
        return random.choice(corner_moves)

    # 5️⃣ Take a side space if nothing else
    return random.choice(available_moves)

def computer_move(board, computer, player):
    """The computer selects the best available move."""
    row, col = find_best_move(board, computer, player)
    return row, col

def is_full(board):
    """Checks if the board is full (draw condition)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"
    
    while True:
        print_board(board)

        # Player Move
        move = input("Enter your move (1-9): ")
        
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Choose a number between 1-9.")
            continue
        
        move = int(move) - 1
        row, col = divmod(move, 3)
        
        if board[row][col] != " ":
            print("That spot is taken. Try again.")
            continue
        
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print("Congratulations! You win!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Smarter Computer Move
        row, col = computer_move(board, computer, player)
        board[row][col] = computer
        print(f"Computer chose {row * 3 + col + 1}")

        if check_winner(board, computer):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
