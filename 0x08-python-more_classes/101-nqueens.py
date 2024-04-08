#!/usr/bin/python3
"""
N Queens problem solver.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, result):
    """
    Solve N Queens problem using backtracking.
    """
    # If all queens are placed, add the solution to result
    if col == n:
        result.append([[i, row.index(1)] for i, row in enumerate(board)])
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            res = solve_nqueens(board, col + 1, n, result) or res

            """Backtrack if placing a queen at board[i][col]
            doesn't lead to a solution"""
            board[i][col] = 0

    return res


def nqueens(n):
    """
    Solve N Queens problem for a given N.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    result = []

    solve_nqueens(board, 0, n, result)

    for solution in result:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
