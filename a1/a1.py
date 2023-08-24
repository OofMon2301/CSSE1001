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


from typing import List, Tuple

Board = List[List[str]]
Pieces = Tuple[int, int]

NAUGHT = "O"
CROSS = "X"


def print_game(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> None:
    """
    Print the current state of the game board, along with the number of remaining pieces for each player.

    Args:
        board (List[List[str]]): A 3x3 list representing the current state of the game board.
        naught_pieces (Tuple[int, int]): A tuple representing the number of remaining naught pieces for each player.
        cross_pieces (Tuple[int, int]): A tuple representing the number of remaining cross pieces for each player.

    Returns:
            None

    Example:
            >>> board = [['O', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', '']]
            >>> naught_pieces = (3, 2)
            >>> cross_pieces = (2, 3)
            >>> print_game(board, naught_pieces, cross_pieces)
            O has: 3, 2
            X has: 2, 3
            1  2  3
                ---------
            1|O|X|O|
                ---------
            2|X|O|X|
                ---------
            3|O|X| |
                ---------
    """
    print(
        NAUGHT
        + " has: "
        + str(naught_pieces)[1:-1]
        + "\n"
        + CROSS
        + " has: "
        + str(cross_pieces)[1:-1]
        + "\n"
    )
    print(
        "   1  2  3\n"
        + "  ---------\n"
        + "1|"
        + board[0][0]
        + "|"
        + board[0][1]
        + "|"
        + board[0][2]
        + "|\n"
        + "  ---------\n"
        + "2|"
        + board[1][0]
        + "|"
        + board[1][1]
        + "|"
        + board[1][2]
        + "|\n"
        + "  ---------\n"
        + "3|"
        + board[2][0]
        + "|"
        + board[2][1]
        + "|"
        + board[2][2]
        + "|\n"
        + "  ---------"
    )


def process_move(move: str) -> Move | None:
    """
    Process the move string and return a tuple with the extracted values converted to
    integers.

    Args:
        move (str): A string representing the move in the format of "row column size".

    Returns:
        Move | None: A tuple with the extracted values converted to integers if
        the input is valid, otherwise None.

    Raises:
        None
    """
    # Split so indexing is easier
    components = move.split()

    # Check if only 3 items
    if len(components) != 3:
        print(INVALID_FORMAT_MESSAGE)
    elif len(components[0]) != 1 or len(components[1]) != 1 or len(components[2]) != 1:
        print(INVALID_FORMAT_MESSAGE)

    # Check if move is valid
    elif not components[0].isdigit():
        print(INVALID_ROW_MESSAGE)
    elif not components[1].isdigit():
        print(INVALID_COLUMN_MESSAGE)
    elif not components[2].isdigit():
        print(INVALID_SIZE_MESSAGE)

    # Check if components are within the range of the board
    elif int(components[0]) > 3 or int(components[0]) <= 0:
        print(INVALID_ROW_MESSAGE)
    elif int(components[1]) > 3 or int(components[1]) <= 0:
        print(INVALID_COLUMN_MESSAGE)
    elif int(components[2] == 0):
        print(INVALID_SIZE_MESSAGE)

    # Return if valid
    else:
        return (int(components[0]) - 1, int(components[1]) - 1, int(components[2]))

    # If invalid
    return None


def get_player_move() -> Move:
    """
    Prompts the user to enter a move and returns a tuple of integers representing the move.

    The input format should be in the following format:
    <row number><space><column number><space><size of the piece to place>
    where row number and column number are 1-indexed and size of the piece to place is a positive integer.

    Returns:
    A tuple of integers representing the move, where the first integer is the row (0-indexed),
    the second integer is the column (0-indexed), and the third integer is the size of the piece to place.

    Example:
    >>> get_player_move()
    Enter your move: 1 2 3
    (0, 1, 3)
    """
    while True:
        # Prompt the user for input
        question = input("Enter your move: ")
        # Input for help
        if question.lower() in ["h", "help"]:
            print(HELP_MESSAGE)

        elif len(question) != 5:
            print(INVALID_FORMAT_MESSAGE)

        elif question[0] not in ["1", "2", "3"]:
            print(INVALID_ROW_MESSAGE)

        elif question[2] not in ["1", "2", "3"]:
            print(INVALID_COLUMN_MESSAGE)

        elif not question[-1].isdigit() or question[-1] == "0":
            print(INVALID_SIZE_MESSAGE)
        else:
            # Return a tuple of integers representing the move
            return (int(question[0]) - 1, int(question[2]) - 1, int(question[-1]))


def check_move(board: Board, pieces_available: Pieces, move: Move) -> bool:
    """
    Check if a move is valid based on the current state of the game.

    This function checks if a move is valid by performing the following checks:
    1. Check if the piece is available
    2. Check if the cell is empty
    3. Check if the piece is larger than the current piece
    4. Check if the move is within the board

    Args:
    board (List[List[str]]): A 3x3 list representing the current state of the Tic Tac Toe board.
    pieces_available (List[str]): A list of available pieces that can be played on the board.
    move (Tuple[int, int, int]): A tuple representing the move to be checked. The first two elements
        represent the row and column indices of the cell to be played, and the third element represents
        the size of the piece to be played.

    Returns:
        bool: True if the move is valid, False otherwise.

    Example:
        >>> board = [['  ', '  ', '  '], ['  ', '  ', '  '], ['  ', '  ', '  ']]
        >>> naught_pieces = [1, 2, 3]
        >>> cross_pieces = [1, 2, 3]
        >>> move = (0, 0, 1)
        >>> check_move(board, naught_pieces, move)
        True

        >>> board = [['X5', '  ', '  '], ['  ', '  ', '  '], ['  ', '  ', '  ']]
        >>> naught_pieces = [1, 2, 3]
        >>> cross_pieces = [1, 2, 3, 6]
        >>> naught_move = (0, 0, 6)
        >>> cross_move = (0, 0, 6)
        >>> check_move(board, naught_pieces, naught_move)
        False
        >>> check_move(board, cross_pieces, cross_move)
        True
    """

    if move[2] not in pieces_available:
        print(INVALID_MOVE_MESSAGE)
        return False
    elif board[move[0]][move[1]] != EMPTY:
        if board[move[0]][move[1]][0] in [NAUGHT, CROSS]:
            if int(board[move[0]][move[1]][-1]) >= move[2]:
                print(INVALID_MOVE_MESSAGE)
                return False
            else:
                return True
        else:
            print(INVALID_MOVE_MESSAGE)
            return False
    elif move[0] not in range(3) or move[1] not in range(3):
        print(INVALID_MOVE_MESSAGE)
        return False
    else:
        return True


def check_win(board: Board) -> str | None:
    """
    Check if there is a winner in the given tic-tac-toe board.

    The function checks all possible ways to win the game: 3 rows, 3 columns, and 2 diagonals.
        If there is a winner, the function returns the symbol of the winner ('X' or 'O').
        If there is no winner yet, the function returns None.

        The function checks all 8 ways to win if they are empty or not.
        If empty, return None. If not empty, return the winner.

        The function checks the rows, columns, and diagonals of the board to determine if there is a winner.
        If there is a winner, the function returns the symbol of the winner ('X' or 'O').
        If there is no winner yet, the function returns None.

    Args:
        board (Board): A 3x3 list of cells representing the current state of the game.
            Each cell is a tuple (symbol, position), where symbol is either 'X', 'O', or ' ' (empty),
            and position is a tuple (row, column) with values between 0 and 2.

    Returns:
        str | None: The symbol of the winner ('X' or 'O'), or None if there is no winner yet.

    Examples:
    # Full board
        >>> board = [['O1', 'X2', 'X4'], ['X6', 'O2', 'X3'], ['X5', 'O3', 'X1']]
        >>> check_win(board)
        'X'
    """

    # None as default
    win = None

    # Check row
    for row in board[0:3]:
        if row[0][0][0] == row[1][0][0] == row[2][0][0] == NAUGHT:
            win = NAUGHT
        elif row[0][0][0] == row[1][0][0] == row[2][0][0] == CROSS:
            win = CROSS

    # Check columns (3 columns) (0, 1, 2)
    for column in range(0, 3):
        if board[0][column][0] == board[1][column][0] == board[2][column][0] == NAUGHT:
            win = NAUGHT
        elif board[0][column][0] == board[1][column][0] == board[2][column][0] == CROSS:
            win = CROSS

    # Check diagonals
    if board[0][0][0] == board[1][1][0] == board[2][2][0] == NAUGHT:
        win = NAUGHT
    elif board[0][0][0] == board[1][1][0] == board[2][2][0] == CROSS:
        win = CROSS

    if board[2][0][0] == board[1][1][0] == board[0][2][0] == NAUGHT:
        win = NAUGHT
    elif board[2][0][0] == board[1][1][0] == board[0][2][0] == CROSS:
        win = CROSS

    return win


def check_stalemate(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> bool:
    """Check whether there is a stalemate.

    A stalemate occurs when there are no empty cells left on the board, and the size of the
    largest available piece is smaller than the largest piece on the board.

    Args:
        board: A 2D list of strings representing the current state of the board.
        naught_pieces: A list of integers representing the sizes of the naught pieces
            available to be placed on the board.
        cross_pieces: A list of integers representing the sizes of the cross pieces
            available to be placed on the board.

    Example:
        >>> board = [
        ...     [EMPTY, EMPTY, 'X1'],
        ...     [EMPTY, 'O2', 'X3'],
        ...     ['O1', 'X2', 'O3']
        ... ]
        >>> naught_pieces = []
        >>> cross_pieces = []
        >>> check_stalemate(board, naught_pieces, cross_pieces)
        True

    Returns:
        A boolean representing whether there is a stalemate.
    """

    # Check if there are no pieces available
    if len(naught_pieces) == 0 and len(cross_pieces) == 0:
        return True

    # Check if there are any empty cells
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    # Check if the pieces available are smaller than all the pieces on the board
    pieces_bigger = 0
    for row in board:
        for cell in row:
            if cell == NAUGHT or CROSS:
                # Get the size of the piece on the board
                piece_size = int(cell[-1])
                if piece_size >= int(max(naught_pieces + cross_pieces)):
                    pieces_bigger += 1
                else:
                    pieces_bigger += 0

    # If all pieces are smaller than those on the board:
    if pieces_bigger == 9:
        return True
    else:
        return False


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

    while True:
        naught_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
        cross_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
        current_player = NAUGHT
        board = initial_state()
        print_game(board, naught_pieces, cross_pieces)

        # Loops until the game encounters a win, stalemate, and changes the player between naughts and crosses.

        while True:
            # Check for win
            win = check_win(board)
            if win == NAUGHT:
                print("O wins!")
                break
            elif win == CROSS:
                print("X wins!")
                break
            # Check for stalemate
            stalemate = check_stalemate(board, naught_pieces, cross_pieces)
            if stalemate:
                print("Stalemate!")
                break
            # Check for player
            if len(naught_pieces) == len(cross_pieces):
                player = NAUGHT
            else:
                player = CROSS
            current_player = player

            print("\n" + current_player + " turn to move\n")
            # Ask for the current move
            move = get_player_move()

            # Make move processable so it's easier to check
            # Move starts at "(0, 0, 1)" for example
            move_string = f"{move[0]+1} {move[1]+1} {move[2]}"

            # Process the move
            processed_move = process_move(move_string)

            # Check if the move can be processed through process_move

            if processed_move is not None:  # Check if the move is valid
                if current_player == NAUGHT:  # Check if the current player is Naught
                    if (
                        check_move(board, naught_pieces, processed_move) == True
                    ):  # Check if the move is valid for Naught
                        if (
                            current_player == NAUGHT
                        ):  # Check if the current player is Naught
                            place_piece(
                                board, NAUGHT, naught_pieces, processed_move
                            )  # Place the piece on the board for Naught
                        else:
                            place_piece(
                                board, CROSS, cross_pieces, processed_move
                            )  # Place the piece on the board for Cross
                        board[processed_move[0]][
                            processed_move[1]
                        ] = player + str(  # Update the board with the new piece
                            processed_move[2]
                        )
                    else:  # If check_move returns False, print the game and continue
                        print_game(board, naught_pieces, cross_pieces)
                        continue
                elif current_player == CROSS:  # Check if the current player is Cross
                    if (
                        check_move(board, cross_pieces, processed_move) == True
                    ):  # Check if the move is valid for Cross
                        if (
                            current_player == NAUGHT
                        ):  # Check if the current player is Naught
                            place_piece(
                                board, NAUGHT, naught_pieces, processed_move
                            )  # Place the piece on the board for Naught
                        else:
                            place_piece(
                                board, CROSS, cross_pieces, processed_move
                            )  # Place the piece on the board for Cross
                        board[processed_move[0]][
                            processed_move[1]
                        ] = player + str(  # Update the board with the new piece
                            processed_move[2]
                        )
                    else:  # If check_move returns False, print the game and continue
                        print_game(board, naught_pieces, cross_pieces)
                        continue
                else:
                    print_game(board, naught_pieces, cross_pieces)
                    continue
            else:
                print_game(board, naught_pieces, cross_pieces)
                continue
            print_game(board, naught_pieces, cross_pieces)

            # Process move, if valid, place piece on the board. Get player move is a tuple return
        continue_game = input("Play again? ")
        if continue_game == "y" or "Y":
            # Reset the game by going to top of while function
            pass
        else:
            break  # Try to terminate the game

        if continue_game not in ["y", "Y"]:
            break
        continue

    # Print the current state of the board after each move


if __name__ == "__main__":
    main()
