import math

# Check winner
def check_winner(board):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] != " ":
            return board[state[0]]
    return None

# Check full board
def is_full(board):
    return " " not in board

# Alpha-Beta Minimax
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == "X": return 1
    elif winner == "O": return -1
    elif is_full(board): return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            move_val = alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = " "
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

# Display board
def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()

# Main game loop
def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe (You are O, AI is X)")
    print_board(board)

    while True:
        # User Move
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = "O"
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 0-8.")

        print_board(board)

        if check_winner(board) == "O":
            print("🎉 You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # AI Move
        ai_move = find_best_move(board)
        board[ai_move] = "X"
        print("AI chooses position", ai_move)
        print_board(board)

        if check_winner(board) == "X":
            print("💻 AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

# Run the game 

play_game()

