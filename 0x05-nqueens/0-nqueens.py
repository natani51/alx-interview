#!/usr/bin/python3
"""
NQueens Solver
"""
import sys


def is_valid_position(board, row, col):
    """Checks if position is valid
    """
    b_size = len(board)
    if sum(board[row]) or sum([board[i][col] for i in range(b_size)]) != 0:
        return False

    for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        r, c = row, col
        while 0 <= r + i < b_size and 0 <= c + j < b_size:
            r, c = r + i, c + j
            if board[r][c]:
                return False
    return True


def place_next_queen(board, row):
    """Places a queen on the board at a valid position if not return False
    """
    st, end = 0, len(board)
    if sum(board[row]) == 1:
        st = board[row].index(1) + 1
        board[row] = [0 for col in range(end)]

    for col in range(st, end):
        if is_valid_position(board, row, col):
            board[row][col] = 1
            return True
    return False


def solve_nqueens(board, solutions=[]):
    """Solves the nqueens problem

    Args:
        n (int): size of board
    """
    n = len(board)
    row = 0
    while row < n:
        if place_next_queen(board, row):
            row += 1
        else:
            if row - 1 < 0:
                break
            row -= 1
        if row == n:
            solutions.append([[row, board[row].index(1)] for row in range(n)])
            row -= 1

    if row == 0:
        return

    solutions.append([[row, board[row].index(1)] for row in range(n)])
    idx = board[0].index(1)
    if idx > -1:
        board = [[0 for _ in range(n)] for row in range(n)]
        board[0][idx] = 1
        solve_nqueens(board, solutions)


def run_solver(n):
    """Runs the solver
    """
    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    solve_nqueens(board, solutions)
    for row in solutions:
        print(row)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        run_solver(n)

    except ValueError:
        print('N must be a number')
        sys.exit(1)
