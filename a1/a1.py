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
    return 3.5


def generate_initial_pieces(num_pieces: int) -> Pieces:
    """Generates the initial pieces.

    Args:
        num_pieces (int): The number of pieces to generate.

    Returns:
        Pieces: The list of generated initial pieces.
    """
    piece = []
    for i in range(num_pieces):
        piece.append(i + 1)
    return piece


def initial_state() -> Board:
    """Generates the initial state of the board.

    Returns:
        Board: The initial state of the board.
    """
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
    """Places a piece on the board.

    Args:
        board (Board): The current state of the board.
        player (str): The player making the move.
        pieces_available (Pieces): The list of available pieces.
        move (Move): The move to make.

    Returns:
        None
    """
    row, column, piece_size = move
    marker = player + str(piece_size)  # Create the marker string
    board[row][column] = marker
    pieces_available.remove(piece_size)


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
    print("O has: " + str(naught_pieces))
    print("X has: " + str(cross_pieces))
    # Board is initial state of board stacked on top of each other
    # Print the column numbers
    columns = ""
    for i in range(1, 4):
        columns += str(i) + " "
    print(columns)

    # Print the horizontal line separator
    separator = ""
    for _ in range(9):
        separator += "-"
    print(separator)

    # Print the rows of the board
    for row_x, row in enumerate(board):
        # Print the row number
        row_number = str(row_x + 1)
        print(row_number + "|", end="")

        # Print each cell's marker (naught, cross, or empty)
        for cell in row:
            centered_marker = cell
            padding = " " * (3 - len(centered_marker))
            print(padding + centered_marker, end="|")
        print()  # Move to the next line after each row


def process_move(move: str) -> Move | None:
    """Attempts to process if valid move and returns a tuple (row, column, piece size) or None.

    Args:
        move (str): The input move string.

    Returns:
        Move | None: Returns a tuple (row, column, piece size) if valid, else None.
    """
    move_parts = move.split()  # Split the move string into parts

    # Check if the move has three parts (row, column, piece size)
    if len(move_parts) != 3:
        print("Invalid move format. Please try again.")
        return None

    # Try to convert the parts to integers
    try:
        row = int(move_parts[0]) - 1  # Convert 1-indexed row to 0-indexed
        column = int(move_parts[1]) - 1  # Convert 1-indexed column to 0-indexed
        piece_size = int(move_parts[2])
    except ValueError:
        print("Invalid move format. Please try again.")
        return None

    # Check if row and column are within valid range
    if row < 0 or row > 2:
        print("Invalid row. Please try again.")
        return None
    if column < 0 or column > 2:
        print("Invalid column. Please try again.")
        return None

    # Check if piece size is valid
    if piece_size < 1 or piece_size > 9:
        print("Invalid piece size. Please try again.")
        return None

    return (row, column, piece_size)  # Return the validated move tuple


def get_player_move() -> None:
    """get_player_move Prompts the user to move.

    Prompts the user to move for an extended amount of time
    until the user is forced to choose, or until there is a valid move.
    """
    pass


def main() -> None:
    """
    This function is the main entry point of the program. It prompts the user for the number of pieces, generates the
    initial pieces, and asks for the initial state of the board. It then prompts the user for the player name for Knots
    and Crosses, and starts the game by asking Knots to make the first move. It then alternates between Knots and Crosses
    until the game is over. The function prints the current state of the board after each move, and announces the winner
    or a draw at the end of the game.

    Parameters:
    None

    Returns:
    None
    """
    # Write your main code here
    # Start by asking the user for the number of pieces
    x = int(input("How many pieces? "))
    pieces = generate_initial_pieces(x)
    print(pieces)
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
