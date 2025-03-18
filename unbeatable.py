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

def is_full(board):
    """Checks if the board is full (draw condition)."""
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing, computer, player):
    """Minimax algorithm for making the AI unbeatable."""
    if check_winner(board, computer):
        return 1  # AI wins
    if check_winner(board, player):
        return -1  # Player wins
    if is_full(board):
        return 0  # It's a draw

    available_moves = get_available_moves(board)

    if is_maximizing:
        best_score = -float("inf")  # AI wants the highest score
        for row, col in available_moves:
            board[row][col] = computer
            score = minimax(board, depth + 1, False, computer, player)
            board[row][col] = " "  # Undo move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")  # Player wants the lowest score
        for row, col in available_moves:
            board[row][col] = player
            score = minimax(board, depth + 1, True, computer, player)
            board[row][col] = " "  # Undo move
            best_score = min(best_score, score)
        return best_score

def find_best_move(board, computer, player):
    """Finds the best move for the computer using Minimax."""
    best_score = -float("inf")
    best_move = None

    for row, col in get_available_moves(board):
        board[row][col] = computer
        score = minimax(board, 0, False, computer, player)  # Run Minimax
        board[row][col] = " "  # Undo move

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move

def computer_move(board, computer, player):
    """AI selects the best move using Minimax."""
    row, col = find_best_move(board, computer, player)
    return row, col

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

        # Perfect Computer Move
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