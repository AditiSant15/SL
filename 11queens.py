def print_solution(board):
    for row in board:
        print(" ".join('1' if cell else '0' for cell in row))
    print()

# ---------------- BACKTRACKING ----------------
def is_safe_bt(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_backtracking(board, col, n):
    if col >= n:
        print("Backtracking Solution:")
        print_solution(board)
        return True  # Return after finding one solution
    res = False
    for i in range(n):
        if is_safe_bt(board, i, col, n):
            board[i][col] = 1
            res = solve_backtracking(board, col + 1, n) or res
            board[i][col] = 0  # BACKTRACK
    return res

def n_queens_backtracking(n):
    board = [[0] * n for _ in range(n)]
    if not solve_backtracking(board, 0, n):
        print("No solution found using Backtracking.")


# ---------------- BRANCH AND BOUND ----------------
def n_queens_branch_and_bound(n):
    board = [[0] * n for _ in range(n)]
    row_lookup = [False] * n
    slash_code = [[0]*n for _ in range(n)]
    backslash_code = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            slash_code[r][c] = r + c
            backslash_code[r][c] = r - c + (n - 1)

    slash_lookup = [False] * (2 * n - 1)
    backslash_lookup = [False] * (2 * n - 1)

    def solve(col):
        if col >= n:
            print("Branch and Bound Solution:")
            print_solution(board)
            return True

        for i in range(n):
            if (not row_lookup[i] and
                not slash_lookup[slash_code[i][col]] and
                not backslash_lookup[backslash_code[i][col]]):

                board[i][col] = 1
                row_lookup[i] = True
                slash_lookup[slash_code[i][col]] = True
                backslash_lookup[backslash_code[i][col]] = True

                if solve(col + 1):
                    return True

                # BACKTRACK
                board[i][col] = 0
                row_lookup[i] = False
                slash_lookup[slash_code[i][col]] = False
                backslash_lookup[backslash_code[i][col]] = False
        return False

    if not solve(0):
        print("No solution found using Branch and Bound.")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    try:
        N = int(input("Enter the value of N for the N-Queens problem: "))
        if N <= 0:
            print("N must be a positive integer.")
        else:
            print("\n--- Solving using Backtracking ---")
            n_queens_backtracking(N)

            print("\n--- Solving using Branch and Bound ---")
            n_queens_branch_and_bound(N)

    except ValueError:
        print("Invalid input. Please enter an integer value for N.")

