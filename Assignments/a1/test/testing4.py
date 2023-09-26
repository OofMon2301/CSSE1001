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
    # Print number of pieces available without square brackets for each player, newline
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

    # Print the board
    # Board = GRID_SIZE x GRID_SIZE
    # Print the board with the pieces in the correct positions
    # Example:
    #   1  2  3\n \
    #  ---------\n \
    # 1|  |  |  |\n \
    #  ---------\n \
    # 2|  |  |  |\n \
    #  ---------\n \
    # 3|  |  |  |\n \
    #  ---------\n \
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


# Define a function named process_move that takes a string argument and returns a tuple or None.
def process_move(move: str) -> Move | None:
    """Attempts to process if valid move and returns a tuple (row, column, piece size) or None.

    Args:
        move (str): The input move string.

    Returns:
        Move | None: Returns a tuple (row, column, piece size) if valid, else None.
    """

    # Split the input string into a list of its three components
    components = move.split()
    # Check if the components are digits or not
    if len(components) != 3:
        print(INVALID_FORMAT_MESSAGE)
    # Check if move a single digit
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
    elif int(components[0]) >= 3 or int(components[0]) <= 0:
        print(INVALID_ROW_MESSAGE)
    elif int(components[1]) >= 3 or int(components[1]) <= 0:
        print(INVALID_COLUMN_MESSAGE)
    elif int(components[2] == 0):
        print(INVALID_SIZE_MESSAGE)
    # Return if valid
    else:
        # If the input is valid, return a tuple with the extracted values converted to integers.
        return (int(components[0]) - 1, int(components[1]) - 1, int(components[2]))
    # If the input is invalid, return None.
    return None


def get_player_move() -> Move:
    """get_player_move Prompts the user to move.

    Prompts the user to move for an extended amount of time
    until the user is forced to choose, or until there is a valid move.
    """
    while True:
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
            return (int(question[0]) - 1, int(question[2]) - 1, int(question[-1]))


def check_move(board: Board, pieces_available: Pieces, move: Move) -> bool:
    # Check if move is valid: 3 Steps
    # 1. Check if the piece is available
    # 2. Check if the cell is empty
    # 3. Check if the piece is larger than the current piece
    if move[2] not in pieces_available:
        print(INVALID_MOVE_MESSAGE)
        return False
    elif board[move[0]][move[1]] != EMPTY:
        if board[move[0]][move[1]] == NAUGHT or CROSS:
            if int(board[move[0]][move[1]][-1]) >= move[2]:
                print(INVALID_MOVE_MESSAGE)
                return False
    else:
        pass
    return True


def check_win(board: Board) -> str | None:
    # Check if there is a winner
    # Should check who won
    # Total of 8 ways to win
    # 3 rows, 3 columns, 2 diagonals
    # Return "None" if no winner

    # Check all 8 ways to win if they are empty or not
    # If empty, return None
    # If not empty, return the winner

    # Check rows

    win = None

    for row in board[0:3]:
        if row[0][0][0] == row[1][0][0] == row[2][0][0] == NAUGHT:
            win = NAUGHT
        elif row[0][0][0] == row[1][0][0] == row[2][0][0] == CROSS:
            win = CROSS
            # Check if the cell is EMPTY or not
            # If EMPTY, then return None

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
    # Check if there is a stalemate
    # Only return true if all empty cells are filled and if the pieces available are smaller
    # Than all the pieces on the board

    # Check if there are any empty cells
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    # Check if the pieces available are smaller than all the pieces on the board
    for row in board:
        for cell in row:
            if cell == NAUGHT or CROSS:
                if int(cell[-1]) > max(naught_pieces + cross_pieces):
                    return True
                else:
                    return False
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
    # Start by asking the user for the number of pieces

    pieces = generate_initial_pieces(PIECES_PER_PLAYER)
    # print(pieces)
    # # Then ask for the initial state of the board
    # y = input("Do you want the Initial state of the board? ")
    # if y == "yes":
    #     print(initial_state())
    # else:
    #     print("Ok")
    # print("Let's play!")
    # Ask for the player name for Knots and Crosses
    naught_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
    cross_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
    current_player = NAUGHT
    board = initial_state()
    print_game(board, naught_pieces, cross_pieces)
    print("\n O Goes first! \n")
    # Loops until the game encounters a win, stalemate, and changes the player between naughts and crosses.
    while True:
        # Check for win
        win = check_win(board)
        if win == NAUGHT:
            print("Naughts win!")
            break
        elif win == CROSS:
            print("Crosses win!")
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
        # Ask for the current move
        move = get_player_move()
        # Process move, if valid, place piece on the board. Get player move is a tuple return
        if check_move(board, pieces, move):
            if current_player == NAUGHT:
                place_piece(board, NAUGHT, naught_pieces, move)
            else:
                place_piece(board, CROSS, cross_pieces, move)
            board[move[0]][move[1]] = player + str(move[2])
        print_game(board, naught_pieces, cross_pieces)
        print("\n" + current_player + " turn to move:\n")
        # Change player
        if current_player == NAUGHT:
            current_player = CROSS
        else:
            current_player = NAUGHT
    # After the game is over, ask the user if they want to play again
    # If yes, then start the game again
    # If no, then exit the program
    continue_game = input("Thanks for playing! \nDo you want to play again? ")
    if continue_game == "yes" or "Yes" or "YES" or "y" or "Y":
        main()
    elif continue_game == "no" or "No" or "NO" or "n" or "N":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input")
        exit()


if __name__ == "__main__":
    main()
