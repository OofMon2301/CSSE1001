""" A fancy tic-tac-toe game for CSSE1001/7030 A1. """
from constants import *

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]


def num_hours() -> float:
    """Return the number of hours you spent on this assignment.

    Returns:
        float: The number of hours.
    """
    return 13.5  # Returns the number of hours spent on the assignment as a float


def generate_initial_pieces(num_pieces: int) -> Pieces:
    """Generates the initial pieces.

    Args:
        num_pieces (int): The number of pieces to generate.

    Returns:
        Pieces: The list of generated initial pieces.
    """
    piece = []  # Create an empty list to hold the pieces
    for i in range(num_pieces):  # Loop through num_pieces times
        piece.append(i + 1)  # Add the piece to the list
    return piece  # Return the list of pieces


def initial_state() -> Board:
    """Generates the initial state of the board.

    Returns:
        Board: The initial state of the board.
    """
    top = []  # Create an empty list to represent the top row of the board
    mid = []  # Create an empty list to represent the middle row of the board
    bot = []  # Create an empty list to represent the bottom row of the board
    for i in range(3):  # Loop through 3 times to create 3 columns for each row
        top.append(EMPTY)  # Add an empty space to the top row
        mid.append(EMPTY)  # Add an empty space to the middle row
        bot.append(EMPTY)  # Add an empty space to the bottom row
    return [
        top,
        mid,
        bot,
    ]  # Return the board as a list of lists, with each row as a list


def place_piece(
    board: Board, player: str, pieces_available: Pieces, move: Move
) -> None:
    """Places a piece on the board.

    Args:
        board (Board): The current state of the board.
        player (str): The player making the move.
        pieces_available (Pieces): The list of available pieces.
        move (Move): The move to make.

    Returns:
        None
    """
    (
        row,
        column,
        piece_size,
    ) = move  # Unpacks the move tuple into row, column, and piece_size variables
    marker = player + str(
        piece_size
    )  # Creates a string marker for the piece using the player and piece size
    board[row][
        column
    ] = marker  # Places the marker on the board at the specified row and column
    pieces_available.remove(
        piece_size
    )  # remove the piece size from the list of available pieces


def print_game(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> None:
    """Prints the current state of the game.

    Args:
        board (Board): The current state of the board.
        naught_pieces (Pieces): The list of available naught pieces.
        cross_pieces (Pieces): The list of available cross pieces.

    Returns:
        None
    """
    # Print updated board after each turn
    # Print number of pieces available without square brackets for each player, newline

    # Print the number of available pieces for each player
    # Print the list of available pieces without square brackets for each player
    # Example: "O has: 1, 2, 3\nX has: 1, 2, 3\n"
    print(
        NAUGHT
        + " has: "
        + str(naught_pieces)[
            1:-1
        ]  # Convert the list to a string and remove the square brackets
        + "\n"
        + CROSS
        + " has: "
        + str(cross_pieces)[
            1:-1
        ]  # Convert the list to a string and remove the square brackets
        + "\n"
    )
