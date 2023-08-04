""" A fancy tic-tac-toe game for CSSE1001/7030 A1. """
from constants import *

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]

# Write your functions here
def num_hours() -> float:
    """Return the number of hours you spent on this assignment.

    Returns:
        float: The number of hours.
    """
    return 0.0

def generate_initial_pieces(num_pieces: int) -> Pieces:
    """Generates the initial pieces.

    Args:
        num_pieces (int): The number of pieces to generate.

    Returns:
        Pieces: How many pieces to generate.
    """
    piece = []
    for i in range(num_pieces):
        piece.append(i+1)
    return piece

def initial_state() -> Board:
    top = []
    mid = []
    bot = []
    for i in range(3):
        top.append(" ")
        mid.append(" ")
        bot.append(" ")
    return [top, mid, bot]

def place_piece(board: Board, player: str,pieces_available: Pieces, move: Move) -> None:
    # Board: Refresh board with uppdated pieces and print
    row, column, piece_size = move
    if piece_size in pieces_available:
        board[row][column] = player + str(piece_size)
        pieces_available.remove(piece_size)
    else:
        print("Invalid move")
    pass

def print_game(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> None:
    # Print updated board after each turn
    print("O has: ", end="")
    for i in range(len(naught_pieces)):
        if i == len(naught_pieces) - 1:
            print(naught_pieces[i])
        else:
            print(naught_pieces[i], end=", ")
    print("X has: ", end="")
    for i in range(len(cross_pieces)):
        if i == len(cross_pieces) - 1:
            print(cross_pieces[i])
        else:
            print(cross_pieces[i], end=", ")
    print("  1 2 3")
    print("  " + "-" * 7)
    for i in range(len(board)):
        row = board[i]
        row_str = str(i + 1) + "|"
        for j in range(len(row)):
            row_str += row[j]
            if j != len(row) - 1:
                row_str += "|"
        row_str += "|"
        print(row_str)
        print("  " + "-" * 7)
        


def main() -> None:
    # Write your main code here
    # Start by asking the user for the number of pieces
    x = int(input("How many pieces? "))
    generate_initial_pieces(x)
    print(generate_initial_pieces(x))
    # Then ask for the initial state of the board
    y = input("Do you want the Initial state of the board? ")
    if y == "yes":
        print(initial_state())
    else:
        print("Ok")
    # Ask for Player X (Cross) or Player O (Nought) to move:
    # player_knots = input("Input player name for Knots: ")
    # player_crosses = input("Input player name for Crosses: ")
    # print(player_knots + ", " + "It is your turn first. Please input your move.")
    # print(player_crosses + ", " + "It is your turn first. Please input your move.")
    
    pass


if __name__ == '__main__':
    main()
