n = 10

board = [[0] * n for i in range(n)]


# Check safe position
def safe(row, col):

    # Check left side
    for i in range(col):

        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col

    while i < n and j >= 0:

        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


# Solve using backtracking
def solve(col):

    if col == n:
        return True

    for row in range(n):

        if safe(row, col):

            board[row][col] = 1

            if solve(col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main
if solve(0):

    for row in board:

        print(row)

else:
    print("No Solution")