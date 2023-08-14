#!/usr/bin/python3
"""
Program to solve the Nqueens challenge.
"""

import sys

def is_safe(board, row, col, N):
    """
    Checks for presence of a queen in the same column
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solves the nqueens problem given an interger N that it iterates over
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solver(board, 0, N, solutions)
    return solutions


def solver(board, row, N, solutions):
    if row == N:
        # solution = ["." * col + "Q" + "." * (N - col - 1) for col in board[row - 1]]
        solution = [(row, col) for col in range(N) if board[row][col] == 1]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solver(board, row + 1, N, solutions)
            board[row][col] = 0

def print_solutions(solutions):
    for solution in solutions:
        for row in solutions:
            print(row)
        print()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])

    except ValueError:
        print("N must be a number")

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)

if __name__ == "__main__":
    main()

