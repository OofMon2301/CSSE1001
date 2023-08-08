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
    return 3.5



def generate_initial_pieces(num_pieces: int) -> Pieces:
    """Generates the initial pieces.

    Args:
        num_pieces (int): The number of pieces to generate.

    Returns:
        Pieces: How many pieces to generate.
    """
    piece = []
    for i in range(num_pieces):
        piece.append(i + 1)
    return piece

def initial_state() -> Board:
    top = []
    mid = []
    bot = []
    for i in range(3):
        top.append(EMPTY)
        mid.append(EMPTY)
        bot.append(EMPTY)
    return [top, mid, bot]


def place_piece(
    board: Board, player: str, pieces_available: Pieces, move: Move
) -> None:
    # Board: Refresh board with updated pieces and print
    row, column, piece_size = move
    if piece_size in pieces_available:
        board[row][column] = player + str(piece_size)
        pieces_available.remove(piece_size)
    else:
        print("Invalid move")
    return


def print_game(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> None:
    # Print updated board after each turn
    print("O has: " + str(naught_pieces))
    print("X has: " + str(cross_pieces))
    # Board is initial state of board stacked on top of each other
    for i in range(3):
        print(board[i])
    return
    
def process_board(move: str) -> Move | None:
    # Process the move input, if invalid, then print related error message
    
    pass

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
# print_game(initial_state(), generate_initial_pieces(x), generate_initial_pieces(x))
    # moving = print(player_knots + ", " + "It is your turn first. Please input your move.")
    # place_piece(initial_state(), player_knots, generate_initial_pieces(x), process_board(moving))
    
    # print(player_crosses + ", " + "It is your turn first. Please input your move.")
    pass


if __name__ == "__main__":
    main()
