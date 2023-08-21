from constants import *
from a1 import check_move

def test_check_move():
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    pieces_available = [1, 2, 3]
    move1 = (0, 0, 1)
    move2 = (1, 1, 2)
    move3 = (2, 2, 3)
    move4 = (0, 0, 4)
    move5 = (1, 1, 1)

    assert check_move(board, pieces_available, move1) == True
    assert check_move(board, pieces_available, move2) == True
    assert check_move(board, pieces_available, move3) == True
    assert check_move(board, pieces_available, move4) == False
    assert check_move(board, pieces_available, move5) == False

    board = [
        [NAUGHT + "1", EMPTY, EMPTY],
        [EMPTY, CROSS + "2", EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    pieces_available = [1, 2, 3]
    move1 = (0, 0, 2)
    move2 = (1, 1, 1)
    move3 = (2, 2, 3)
    move4 = (0, 0, 1)
    move5 = (1, 1, 3)

    assert check_move(board, pieces_available, move1) == False
    assert check_move(board, pieces_available, move2) == False
    assert check_move(board, pieces_available, move3) == True
    assert check_move(board, pieces_available, move4) == False
    assert check_move(board, pieces_available, move5) == True
