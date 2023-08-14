#!/usr/bin/env python3

"""
N Queens Problem Solver
"""

import sys

def print_solution(solution):
    """Print the solutions in the specified format"""
    for row, col in solution:
        print("[{}, {}]".format(row, col), end=' ')
    print()

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queens in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, n, solutions):
    """Solve the N Queens problem using backtracking"""
    if row == n:
        solution = [(r, c) for r in range(n) for c in range(n) if board[r][c] == 1]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0


def nqueens(n):
    """Solve the N Queens problem for a given N"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
