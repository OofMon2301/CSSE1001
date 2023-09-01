from a2_support import *


# Write your classes here
class Tile:
    """An abstract class from which all instantiable types of tiles inherit.

    Provides the default tile behaviour. Can be inhereted or overwritten by specific
    types of tiles.
    __init__ methods for all tiles do not take any arguments except 'self'.
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
        return FLOOR


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
        return WALL

    def __str__(self) -> str:
        # Return "W" for wall
        return WALL

    def __repr__(self) -> str:
        # Return "W" for wall
        return WALL


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
        By default, entities are movable.
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
    player_position = (1, 1)
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
    """

    def __init__(self, maze_file: str) -> None:
        """Initialize a SokobanModel object.

        Should read the given maze file, call convert_maze function to get the grid,
        entities, and player position, and initialize the player object.

        Parameters:
            maze_file: The path to the maze file (e.g. 'maze_files/maze1.txt')
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
        """Return the maze."""
        return self._maze

    def get_entities(self) -> Entities:
        """Return the entities."""
        return self._entities

    def get_player_position(self) -> tuple[int, int]:
        """Return the player position."""
        return self._player_position

    def get_player_moves_remaining(self) -> int:
        """Return the player moves remaining."""
        return self._player.get_moves_remaining()

    def get_player_strength(self) -> int:
        """Return the player strength."""
        return self._player.get_strength()

    def attempt_move(self, direction: str) -> bool:
        """attempt_move Handles trying to move the player in the given direction.

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
        if direction.lower() not in DIRECTION_DELTAS:
            return False
        # Call direction to value in DIRECTION_DELTAS
        # direction = DIRECTION_DELTAS[direction.lower()]
        # Check if the path that the player is moving to has a wall

    def has_won(self) -> bool:
        """Return True if the player has won, False otherwise.

        The player has won if all goal positions are filled with crates.
        """
        # Check if all goals are filled
        for goal in self._goal_position:
            if not self._maze[goal[0]][goal[1]].is_filled():
                return False
        return True


def main():
    # uncomment the lines below once you've written your Sokoban class
    # game = Sokoban('maze_files/maze1.txt')
    # game.play_game()
    pass


if __name__ == "__main__":
    main()
