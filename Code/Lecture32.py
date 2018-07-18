# pylint: disable=c
def is_safe(board, row):
    """Given a partially filled safe board, determine whether placing a
    queen on the next column for the given row is safe.
    Return True if the move is safe, False otherwise.

    Args:
    board--a tuple of row-indecies denoting a partially filled safe board
    row--the proposed row number in the next column to place the queen at.
   """
    if row in board:
        return False
    size = len(board)
    for col_ind in range(size):
        # Check the diagonals - if they are the same number of columns and rows
        # apart, then it is under attack diagonally
        if abs(row - board[col_ind]) == size - col_ind:
            return False
    return True


def n_queens(size, board):
    """Solve the n-queens problem recursively

    Return a tuple with a length==size representing the solution

    Args:
    size--the size (nxn) of the board. 8 is the classical problem
    board--a tuple representing the board so far
    """
    # base case
    if len(board) == size:
        return board
    # recursive case
    for row in range(size):
        if is_safe(board, row):
            new_board = board + (row, )  #singleton tuple
            solution = n_queens(size, new_board)
            if solution != None:
                return solution
    # None represents 'stuck' or no solution for this board so far
    return None


def eightqueens():
    return n_queens(8, tuple())


eightqueens()
