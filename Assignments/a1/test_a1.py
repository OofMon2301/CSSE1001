from constants import *

board = [[EMPTY, EMPTY, EMPTY], [EMPTY, "X2", EMPTY], [EMPTY, EMPTY, EMPTY]]

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]


def check_win(board: Board) -> str | None:
    # Check if there is a winner
    # Should check who won
    # Total of 8 ways to win
    # 3 rows, 3 columns, 2 diagonals
    # Return "None" if no winner

    # Check rows
    for row in board[0:3]:
        if row[0][0][0] == row[1][0][0] == row[2][0][0]:
            win = row[0][0][0]
            return win
    # Check if first row, column and last row, column is empty
    # If so, then return None
    if (
        board[0][0] == EMPTY
        and board[0][2] == EMPTY
        and board[2][0] == EMPTY
        and board[2][2] == EMPTY
    ):
        return None
    # Check columns (3 columns) (0, 1, 2)
    for column in range(0, 3):
        if board[0][column][0] == board[1][column][0] == board[2][column][0]:
            win1 = board[0][column][0]
            return win1
    # Check diagonals
    if board[0][0][0] == board[1][1][0] == board[2][2][0]:
        win2 = board[0][0][0]
        return win2
    elif board[2][0][0] == board[1][1][0] == board[0][2][0]:
        win3 = board[2][0][0]
        return win3
    # If no win1, win2, win3, return None
    else:
        return None


check_win(board)
