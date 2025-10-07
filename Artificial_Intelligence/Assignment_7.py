N = 8  # Board size (8x8)

def print_board(board):
    """Utility to print the chessboard."""
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""

    # Check this column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row=0):
    """Backtracking algorithm to solve N-Queens."""
    if row == N:  # All queens placed
        print("Solution found:")
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_nqueens(board, row + 1):  # Recurse
                return True
            board[row][col] = 0  # Backtrack

    return False

# Driver
board = [[0] * N for _ in range(N)]
if not solve_nqueens(board):
    print("No solution exists")