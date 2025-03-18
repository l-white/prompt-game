import random

DIFFICULTY = "easy"  # Change to "easy", "medium", or "hard"

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

def make_mistake(board, computer, player):
    """Makes a strategic but non-perfect move."""
    available_moves = get_available_moves(board)

    # Try to block if the player is about to win
    for row, col in available_moves:
        board[row][col] = player
        if check_winner(board, player):
            board[row][col] = " "
            return row, col  # Block player's win
        board[row][col] = " "

    # Otherwise, pick center, corner, or a random move
    if (1, 1) in available_moves:
        return (1, 1)
    
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    corner_moves = [move for move in corners if move in available_moves]
    if corner_moves:
        return random.choice(corner_moves)

    return random.choice(available_moves)  # Last resort

def computer_move(board, computer, player):
    """AI selects a move with a chance of making a mistake."""
    
    # Define difficulty levels
    mistake_chance = {
        "easy": 0.5,    # 50% of the time, AI makes a mistake
        "medium": 0.2,  # 20% mistake chance
        "hard": 0.05    # 5% mistake chance
    }

    if random.random() < mistake_chance[DIFFICULTY]:  # Random chance to make a mistake
        return make_mistake(board, computer, player)
    else:
        return find_best_move(board, computer, player)  # Play optimally

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

        # AI Makes a Move with a Chance of Mistake
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
