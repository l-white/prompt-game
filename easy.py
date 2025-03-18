import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def computer_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)  # Random AI

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
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
        
        # Computer Move
        row, col = computer_move(board)
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
