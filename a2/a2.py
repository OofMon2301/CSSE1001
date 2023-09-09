from a2_support import *


# Write your classes here
class Tile:
    """An abstract class from which all instantiable types of tiles inherit.

    Provides the default tile behaviour. Can be inhereted or overwritten by specific
    types of tiles.
    """

    def __init__(self) -> None:
        """Initialize a Tile object."""
        self._can_move = True
        self._type = "Abstract Tile"

    def is_blocking(self) -> bool:
        """Return True if the tile is blocking, False otherwise.
        By default, tiles are non-blocking.
        """
        return not self._can_move

    def get_type(self) -> str:
        """Return the type of the tile.

        For the abstract Tile class, this method returns the string 'Abstract Tile'.
        For instantiable subclasses, this method should return the single letter
        constant corresponding to the class.
        """
        return "Abstract Tile"

    def __str__(self) -> str:
        """Return a string representation of the tile. In most cases, this will be the
        same string as would be returned by get_type().
        """
        return self._type

    def __repr__(self) -> str:
        """Return a string representation of the tile.
        Operates identically to __str__().
        """
        return self._type


class Floor(Tile):
    """Floor tile class. Is a basic type of tile that represents an empty space.


    Entities can freely move on this space, is non-blocking and is represented by a
    single space character.

    Args:
        Tile (_type_): a tile object

    Examples:
        >>> floor.is_blocking()
        False
        >>> floor = Floor()
        >>> floor.get_type()
        ' '
        >>> str(floor)
        ' '
        >>> floor # note that the below output contains a space character without
        ... quotation marks
    """

    def __init__(self) -> None:
        """Initialize a Floor object."""
        self._can_move = True
        self._type = FLOOR

    def is_blocking(self) -> bool:
        # Return False for floor
        return False

    def get_type(self) -> str:
        # Return " " for floor
        return self._type


class Wall(Tile):
    """Wall tile class. Is a basic type of tile that represents a wall.

    Wall tiles are blocking, and are represented by the character "W".

    Args:
        Tile (_type_): A tile object

    Examples:
        >>> wall = Wall()
        >>> wall.is_blocking()
        True
        >>> wall.get_type()
        'W'
        >>> str(wall)
        'W'
        >>> wall
        W
    """

    def __init__(self) -> None:
        """Initialize a Wall object."""
        self._can_move = False
        self._type = WALL

    def get_type(self) -> str:
        # Return "W" for wall
        return self._type

    def __str__(self) -> str:
        # Return "W" for wall
        return self._type

    def __repr__(self) -> str:
        # Return "W" for wall
        return self._type


class Goal(Tile):
    """Goal is a basic type of tile that represents a goal location for a box.

    Goal tiles are non-blocking, and are represented by the character "G".
    Goal tiles can either be filled by a box or empty.
    Goal tiles start unfilled, and can be filled by a box.
    If goal tile is unfilled, __str__ and __repr__ will return "G".
    When goal tile is filled, __str__ and __repr__ will return "X".

    Args:
        Tile (_type_): _description_
    """

    def __init__(self) -> None:
        """Initialize a Goal object."""
        self._can_move = True
        self._type = GOAL
        self._filled = False

    def is_blocking(self) -> bool:
        # Return False for goal
        return False

    def get_type(self) -> str:
        # Return "G" for empty goal
        return self._type

    def is_filled(self) -> bool:
        # Return True if goal is filled
        return self._filled

    def fill(self) -> None:
        # Fill goal
        self._filled = True

    def __str__(self) -> str:
        # Return "X" if goal is filled
        if self._filled:
            return FILLED_GOAL
        else:
            return self._type

    def __repr__(self) -> str:
        # Return "X" if goal is filled
        if self._filled:
            return FILLED_GOAL
        else:
            return self._type


class Entity:
    """Abstract class for all entities in the game.

    The __init__ methods for this class do not take any arguments except 'self'.
    """

    def __init__(self) -> None:
        """Initialize an Entity object."""
        self._type = "Abstract Entity"
        self._tile = None

    def get_type(self) -> str:
        """Return the type of the entity.

        For the abstract Entity class, this method returns the string 'Abstract Entity'.
        For instantiable subclasses, this method should return the single letter
        constant corresponding to the class.
        """
        return self._type

    def is_movable(self) -> bool:
        """Return True if the entity is movable, False otherwise.
        By default, entities are not movable.
        """
        return False

    def __str__(self) -> str:
        """Return a string representation of the entity. In most cases, this will be the
        same string as would be returned by get_type().
        """
        return self._type

    def __repr__(self) -> str:
        """Return a string representation of the entity.
        Operates identically to __str__().
        """
        return self._type


class Crate(Entity):
    """Crate is a basic type of entity that represents a crate.

    A moveable entity, represented by the character "C" in get_type().
    Crates have a strength value, which represents the strength the player needs to
    push the crate.
    The string representation of a crate should be the string version of its strength
    value.
    Strength of the crate will always be between 0 and 9, inclusive.

    Blocking players from moving crates that they are not strong enough to move should
    not be handled here.
    A crate only needs to be aware of its own strength, and provide interface for
    which the model class can access the information.

    Args:
        Entity (_type_): _description_

    Examples:
        >>> crate = Crate(4)
        >>> crate.get_type()
        'C'
        >>> crate.is_movable()
        True
        >>> str(crate)
        '4'
        >>> crate # Note that this is a string displaying without quotation marks
        4
        >>> crate.get_strength() # Note that this is an integer
        4
    """

    def __init__(self, strength) -> None:
        super().__init__()
        self._type = CRATE
        self._strength = strength

    def get_type(self) -> str:
        # Return "C" for crate
        return self._type

    def is_movable(self) -> bool:
        # Return True for crate
        return True

    def get_strength(self) -> int:
        # Return strength of crate
        return self._strength

    def __str__(self) -> str:
        # Return strength of crate
        return str(self._strength)

    def __repr__(self) -> str:
        # Return strength of crate
        return str(self._strength)


class Potion(Entity):
    """An abstract class from which all instantiable types of potions must implement.

    The __init__ methods for this class do not take any arguments except 'self'.
    Since this class inherits from Entity, it (along with subclasses) shoudl also provide
    all methods and attributes from Entity.

    Potions are not moveable.
    An abstract potion is represented by 'Potion' and has no effect.

    """

    def __init__(self) -> None:
        """Initialize a Potion object."""
        super().__init__()
        self._type = "Potion"
        self._effect = {}

    def effect(self) -> dict[str, int]:
        """Return the effect of the potion."""
        return self._effect

    def __str__(self) -> str:
        """Return a string representation of the potion."""
        return self._type

    def __repr__(self) -> str:
        """Return a string representation of the potion."""
        return self._type

    def get_type(self) -> str:
        """Return the type of the potion."""
        return self._type

    def is_movable(self) -> bool:
        """Return True if the potion is movable, False otherwise."""
        return False


class StrengthPotion(Potion):
    """StrengthPotion Represented by string "S"

    Provides the player with 2 extra strength points.


    Args:
        Potion (_type_): a potion object
    """

    def __init__(self) -> None:
        """Initialize a StrengthPotion object."""
        super().__init__()
        self._type = STRENGTH_POTION
        self._effect = {"strength": 2}


class MovePotion(Potion):
    """MovePotion Represented by string "M"

    Provides the player with 1 extra move point.


    Args:
        Potion (_type_): a potion object
    """

    def __init__(self) -> None:
        """Initialize a MovePotion object."""
        super().__init__()
        self._type = MOVE_POTION
        self._effect = {"moves": 5}


class FancyPotion(Potion):
    """FancyPotion Represented by string "F"

    Provides the player with 2 extra move point and 2 extra strength points.


    Args:
        Potion (_type_): a potion object
    """

    def __init__(self) -> None:
        """Initialize a FancyPotion object."""
        super().__init__()
        self._type = FANCY_POTION
        self._effect = {"moves": 2, "strength": 2}


class Player(Entity):
    """Player A moveable entity that is represented by the character "P".

    A player instance is constructed with a starting strength and initial number of moves.
    The player's strength and moves can be increased by collecting potions.
    A player is only moveable if they have a positive number of moves.


    Args:
        Entity (_type_): _description_
    """

    def __init__(self, start_strength: int, moves_remaining: int) -> None:
        """__init__
        Ensure any code from Entity is run, and set the player strength to start_strength
        and moves to moves_remaining.
        """
        super().__init__()
        self._type = PLAYER
        self._start_strength = start_strength
        self._start_moves = moves_remaining

    def get_strength(self) -> int:
        """Return the player's strength."""
        return self._start_strength

    def add_strength(self, amount: int) -> None:
        """Add strength to the player."""
        self._start_strength += amount

    def get_moves_remaining(self) -> int:
        """Return the player's moves remaining."""
        return self._start_moves

    def add_moves_remaining(self, amount: int) -> None:
        """Add moves to the player."""
        self._start_moves += amount

    def apply_effect(self, potion_effect: dict[str, int]) -> None:
        """Apply the effect of a potion to the player."""
        if "strength" in potion_effect:
            self.add_strength(potion_effect["strength"])
        if "moves" in potion_effect:
            self.add_moves_remaining(potion_effect["moves"])


def convert_maze(game: list[list[str]]) -> tuple[Grid, Entities, Position]:
    """Convert a list of lists of strings into a Grid, Entities, and Position.

    The read_file in a2_support will return a tuple containing a representation of the
    maze (including tiles and entities), and the player stats (strength and moves).

    The representation of the maze is in the format list[list[str]], where each string
    is a character representing a tile or entity at that position.

    If entity is present at a position, it is assumed that the tile underneath is a
    floor tile.

    1. A list of lists of Tile instances, representing the tiles on the grid.
    2. A dictionary mapping (row, column) positions to Entity instances. This dictionary
    only contains positions on which entities exist, and does not contain the player,
    despite the player being an entity.
    3. A tuple containing the (row, column) position of the player.

    Args:
        game (list[list[str]]): A list of lists of strings representing the game.

    Returns:
        tuple[Grid, Entities, Position]: A tuple containing the three structures
        mentioned above (in order).

    Examples:
        >>> raw_maze, player_stats = read_file('maze_files/maze1.txt')
        >>> maze, entities, player_position = convert_maze(raw_maze)
        >>> maze
        [[W, W, W, W, W, W, W, W], [W, , , , W, , , W], [W, , , , W, , , W],
        [W, , , , W, G, , W], [W, , , , , , , W], [W, , , , , , , W],
        [W, W, W, W, W, W, W, W]]
        >>> entities
        {(3, 2): 1}
        >>> player_position
        (1, 1)
    """
    # Check where player is and make player_position the tuple of the position
    for i, row in enumerate(game):
        for j, cell in enumerate(row):
            if cell == PLAYER:
                player_position = (i, j)
    # Creates dictionary of entities
    entities = {}
    # Check if cell is entity
    for i, row in enumerate(game):
        for j, cell in enumerate(row):
            if cell.isdigit():
                entities[(i, j)] = int(cell)

    return game, entities, player_position


class SokobanModel:
    """A class for maintaining the game state and applying game logic.

    The SokobanModel class is responsible for maintaining the state of the game.

    Attributes:
        _maze (Grid): A 2D list representing the maze.
        _entities (Entities): A dictionary mapping the positions of entities in the maze to their respective objects.
        _player_position (tuple[int, int]): A tuple representing the position of the player in the maze.
        _player (Player): An object representing the player in the game.
        _moves (int): An integer representing the number of moves the player has made.
        _strength (int): An integer representing the strength of the player.
        _potion (int): An integer representing the number of potions the player has.
        _crate (int): An integer representing the number of crates in the maze.
        _goal (int): An integer representing the number of goals in the maze.
        _goal_position (list[tuple[int, int]]): A list of tuples representing the positions of the goals in the maze.
        _crate_position (list[tuple[int, int]]): A list of tuples representing the positions of the crates in the maze.
        _potion_position (list[tuple[int, int]]): A list of tuples representing the positions of the potions in the maze.
    """

    def __init__(self, maze_file: str) -> None:
        """Initialize a SokobanModel object.

        Should read the given maze file, call convert_maze function to get the grid,
        entities, and player position, and initialize the player object.

        Args:
            maze_file (str): The path to the maze file (e.g. 'maze_files/maze1.txt')
        """
        self._maze, self._entities, self._player_position = convert_maze(
            read_file(maze_file)[0]
        )
        self._player = Player(read_file(maze_file)[1][0], read_file(maze_file)[1][1])
        self._moves = 0
        self._strength = 0
        self._potion = 0
        self._crate = 0
        self._goal = 0
        # As tuples where the position is
        self._goal_position = []
        self._crate_position = []
        self._potion_position = []

    def get_maze(self) -> Grid:
        """Return the maze.

        Returns:
            Grid: A 2D list representing the maze.
        """
        return self._maze

    def get_entities(self) -> Entities:
        """Return a dictionary mapping and updating the player position.

        Returns:
            Entities: A dictonary mapping the positions of entities in the maze to their respective objects.
        """
        return self._entities

    def get_player_position(self) -> tuple[int, int]:
        """Return the player position.

        Returns:
            tuple[int, int]: A tuple representing the position of the player in the maze.
        """
        return self._player_position

    def get_player_moves_remaining(self) -> int:
        """Return the player moves remaining.

        Returns:
            int: An integer representing the number of moves the player has remaining.
        """
        return self._player.get_moves_remaining()

    def get_player_strength(self) -> int:
        """Return the player strength.

        Returns:
            int: An integer representing the strength of the player.
        """
        return self._player.get_strength()

    def attempt_move(self, direction: str) -> bool:
        """Handles trying to move the player in the given direction.


        Tries to move the player in the given direction if possible. Any flow on effects
        from that move. (e.g. pushing a crate) should be handled here. The method should
        return True if a move occurred successfully, and False otherwise.

        The move has to be executed in this order:

        1. If the direction is not a valid move direction, or the position would be out of
        bounds or blocked, return False.

        2. If the move would cause the player to move to a crate, check if the crate can
        be pushed. If the crate can be pushed, move the crate and the player. If the crate
        cannot be pushed, return False. The moved crate would also have to be contained
        in bounds of the maze, or this returns False.

        3. If the move would cause the player to move to a potion, apply the effect of the
        player and remove the potion from the maze.

        4. If the move is valid, then update the player position and decrease the player's
        moves remaining by 1. Return True.

        Args:
            direction (str): a string representing the direction to move in. This can be
            one of the constants UP, DOWN, LEFT, or RIGHT.

        Returns:
            bool: Return True if the player moved successfully, False otherwise.
        """
        # Process all move directions
        current_position = self.get_player_position()

        # Step 1: Check if direction is valid
        if direction not in DIRECTION_DELTAS:
            return False

        # Step 2: Check if player is blocked by wall
        if (
            self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
                current_position[1] + DIRECTION_DELTAS[direction][1]
            ]
            == WALL
        ):
            return False

        # If moving the player to a crate, check if crate can be pushed
        if self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
            current_position[1] + DIRECTION_DELTAS[direction][1]
        ].isdigit():
            # Check if player strength is strictly greater than crate strength
            if self._player.get_strength() > int(
                self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
                    current_position[1] + DIRECTION_DELTAS[direction][1]
                ]
            ):
                # Check if the crate will move to a .is_blocking() tile
                if (
                    self._maze[
                        current_position[0] + 2 * DIRECTION_DELTAS[direction][0]
                    ][
                        current_position[1] + 2 * DIRECTION_DELTAS[direction][1]
                    ].is_blocking()
                    == False
                ):
                    # Move crate to new position visually and in maze
                    self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
                        current_position[1] + DIRECTION_DELTAS[direction][1]
                    ] = FLOOR
                    self._maze[
                        current_position[0] + 2 * DIRECTION_DELTAS[direction][0]
                    ][current_position[1] + 2 * DIRECTION_DELTAS[direction][1]] = CRATE

                    # Update crate position
                    self._crate_position.append(
                        (
                            current_position[0] + DIRECTION_DELTAS[direction][0],
                            current_position[1] + DIRECTION_DELTAS[direction][1],
                        )
                    )
                else:
                    return False

        # Step 3: Apply potion effect
        elif self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
            current_position[1] + DIRECTION_DELTAS[direction][1]
        ] in [STRENGTH_POTION, MOVE_POTION, FANCY_POTION]:
            # Apply potion effect
            self._player.apply_effect(
                self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
                    current_position[1] + DIRECTION_DELTAS[direction][1]
                ].effect()
            )
            # Remove potion from maze
            self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
                current_position[1] + DIRECTION_DELTAS[direction][1]
            ] = FLOOR

        # Step 4: Update player position
        if self._maze[current_position[0]][current_position[1]] != GOAL:
            self._maze[current_position[0]][current_position[1]] = FLOOR
        else:
            self._maze[current_position[0]][current_position[1]] = GOAL

        self._player_position = (
            current_position[0] + DIRECTION_DELTAS[direction][0],
            current_position[1] + DIRECTION_DELTAS[direction][1],
        )

        # Update get_entities with crate position
        self._entities = self.get_entities()

        # Decrease player moves remaining by 1
        self._player.add_moves_remaining(-1)
        return True

    def has_won(self) -> bool:
        """Return True if the player has won, False otherwise.

        The player has won if all goal positions are filled with crates.
        """
        winning = False
        # Check if all goal positions are filled with crates
        if FILLED_GOAL in self._maze:
            winning = True
        return winning


class Sokoban:
    """Represents the controller class for the game.

    Responsible for instantiating the model and view class. Also handles events such as
    user input and communication between the model and view.
    """

    def __init__(self, maze_file: str) -> None:
        """Initialize a Sokoban object.

        Should initialize the model and view classes, and call the view's draw method.
        """
        self._model = SokobanModel(maze_file)
        self._view = SokobanView()

    def display(self) -> None:
        """Display the current state of the game."""
        self._view.display_game(
            self._model.get_maze(),
            self._model.get_entities(),
            self._model.get_player_position(),
        )
        self._view.display_stats(
            self._model.get_player_moves_remaining(), self._model.get_player_strength()
        )

    def play_game(self) -> None:
        """play_game Runs the main function of the game.

        Runs the main loop and follows this behaviour:
        While the game is still going, repeat the following procedure:
        1. If the game has been won, display the game state and the message 'You won!',
        and return.
        2. If the game has been lost, display the message 'You lost!', and return.
        3. Display the game state.
        4. Prompt the user for input 'Enter move: '.
        5. If the move is 'q', return, otherwise attempt to move the player in the given
        direction.
        6. If the move was invalid, display the message 'Invalid move.\n'.
        """
        while True:
            if self._model.has_won():
                self.display()
                print("You won!")
                return
            if self._model.get_player_moves_remaining() == 0:
                print("You lost!")
                return
            self.display()
            direction = input("Enter move: ")
            if direction == "q":
                return
            elif not self._model.attempt_move(direction):
                print("Invalid move.\n")


def main():
    # uncomment the lines below once you've written your Sokoban class
    game = Sokoban("a2/maze_files/maze1.txt")
    game.play_game()
    pass


if __name__ == "__main__":
    main()
