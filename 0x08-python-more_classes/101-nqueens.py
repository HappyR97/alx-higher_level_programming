#!/usr/bin/python3

"""

This module defines a NQueens class

"""


class NQueens:
    """Class to solve NQueens"""

    def __init__(self, N):
        """Initialize values"""
        self.__N = N
        self.solutions = []

    def safe_position(self, position, board):
        """ Checks if a position is safe to place queen """
        [x, y] = position
        if x >= self.__N or y >= self.__N or x < 0 or y < 0:
            return False

        for queen in board:
            [queen_x, queen_y] = queen
            if queen_x == x or queen_y == y:
                return False
            if (queen_x - queen_y == x - y) or (queen_x + queen_y == x + y):
                return False
        return True

    def backtrack(self, board, column):
        """ Backtracking algorithm to solve NQUeens """
        if column == self.__N:
            self.solutions.append(board.copy())
            return True

        for row in range(self.__N):
            position = [row, column]
            if self.safe_position(position, board):
                board.append(position)
                self.backtrack(board, column + 1)
                board.pop()

        return False

    def solve(self):
        """ Solves NQueens """
        board = []
        self.backtrack(board, 0)
        for solution in self.solutions:
            print(solution)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    NQueens(N).solve()
    del NQueens
