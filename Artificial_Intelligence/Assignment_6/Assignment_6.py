import math

# Print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

# Check winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != "_":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "_":
        return board[0][2]
    return None

# Check if full
def is_full(board):
    return all(cell != "_" for row in board for cell in row)

# Minimax evaluation
def evaluate(board):
    winner = check_winner(board)
    if winner == "X":  # AI
        return 1
    elif winner == "O":  # Human
        return -1
    return 0

# Get all possible moves
def get_children(board, player):
    children = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                children.append(new_board)
    return children

# Minimax function
def minimax(board, depth, maximizing_player):
    if check_winner(board) or is_full(board):
        return evaluate(board), board

    if maximizing_player:  # AI is X
        max_eval = -math.inf
        best_board = None
        for child in get_children(board, "X"):
            eval_value, _ = minimax(child, depth - 1, False)
            if eval_value > max_eval:
                max_eval = eval_value
                best_board = child
        return max_eval, best_board
    else:  # Human is O
        min_eval = math.inf
        best_board = None
        for child in get_children(board, "O"):
            eval_value, _ = minimax(child, depth - 1, True)
            if eval_value < min_eval:
                min_eval = eval_value
                best_board = child
        return min_eval, best_board

# Game loop
board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]

while True:
    print_board(board)

    if check_winner(board) or is_full(board):
        break

    # Human move
    row, col = map(int, input("Enter row and col (0-2): ").split())
    if row or col :
        print("Please enter row & col both!")
    if board[row][col] == "_":
        board[row][col] = "O"

    print_board(board)

    if check_winner(board) or is_full(board):
        break

    # AI move using minimax
    _, board = minimax(board, depth=5, maximizing_player=True)

winner = check_winner(board)
if winner:
    print(f"{winner} wins!")
else:
    print("It's a draw!")
