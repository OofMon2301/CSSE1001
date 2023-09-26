from a2_support import *

class Tile(object): #Abstract Class
    """Tile _summary_

    An abstract class from which all instantiable types of tiles inheret. 
    Provides the default tile behaviour, which can be inhereted or overwritten
    by specific types of tiles. The __init__ methods for all tiles do not take any
    arguments beyond self.

    Args:
        object (_type_): _description_

    Example: #take from task sheet
    """

    def __init__(self):
        """
        Initalises the Tile class to state that by default, Tiles are not blocking
        A tile is blocking if an entity would not be able to move onto that tile.
        """
        self.blocking = False

    def is_blocking(self) -> bool:
        """Returns true when a tile is blocking.

        This function returns true when a tile is blocking.  A tile is blocking if an
        entity would not be able to move onto that tile.
        By default, tiles are non-blocking."
        """

        return self.blocking
    
    
    def get_type(self) -> str:
        """
        A string representing the type of this tile. For the abstract 
        Tile class, this method returns the string
        'Abstract Tile'. For instantiable subclasses, this method should return
        the single letter constant corresponding
        to that class.

        Returns:
            'Abstract Tile' for the abstract Tile class.
            The single letter constant corresponding to instantiable subclasses.
        """

        if type(self) == Tile:
            return ('Abstract Tile')
        else: 
            return type(self)

    def __str__(self) -> str:
        """
        Returns a string representing the type of this tile. In most cases, 
        this will be the same string as would be returned by get_type.

        Returns:
            str: 'Abstract Tile' for the abstract Tile class.
            str: The single letter constant corresponding to instantiable subclasses.
        """

        if type(self) == Tile:
            return str('Abstract Tile')
        else: 
            return str(type(self))
    
    def __repr__(self) -> str:
    
        """
        Operates identically to the __str__ method.

        Returns:
            str: 'Abstract Tile' for the abstract Tile class.
            str: The single letter constant corresponding to instantiable subclasses.
        """

        if type(self) == Tile:
            return str('Abstract Tile')
        else: 
            return str(type(self))
        
class Floor(Tile): #Class
    """
    Inherits from tile.
    Floor is a basic type of tile that represents an empty space on which entities can
    freely move. It is non-blocking and is represented by a single space character.

    Args:
        Tile (_type_): _description_
    """
    def get_type(self) -> str:
        """
        The type for FLOOR that is defined in a2_support.py

        Returns:
            The single letter constant corresponding to instantiable subclasses.
        """

        return FLOOR
        
    def __str__(self) -> str:
        """
        FLOOR is non-blocking and is represented by a single space character.

        Returns:
            str: FLOOR is defined in a2_support.py
        """

        return str(FLOOR)

    def __repr__(self) -> str:
        """
        FLOOR is non-blocking and is represented by a single space character.

        Returns:
            str: FLOOR is defined in a2_support.py
        """

        return str(FLOOR)

class Wall(Tile): #Class
    """
    Inherits from Tile.
    Wall is a type of tile that represents a wall through which entities cannot pass.
    Wall tiles are blocking, and are represented by the character 'W'.

    Args:
        Tile (_type_): _description_
    """

    def __init__(self):
        """
        Reinitalises the the Wall class to state that by default, Walls are blocking
        A tile is blocking if an entity would not be able to move onto that tile.
        """
        self.blocking = True

    def get_type(self) -> str:
        """
        The type for WALL that is defined in a2_support.py

        Returns:
            The single letter constant corresponding to instantiable subclasses.
        """

        return WALL
        
    def __str__(self) -> str:
        """
        WALL is blocking and is represented by a 'W'.

        Returns:
            str: wall is defined in a2_support.py
        """

        return str(WALL)

    def __repr__(self) -> str:
        """
        WALL is blocking and is represented by a 'W'.

        Returns:
            str: WALL defined in a2_support.py
        """

        return str(WALL)
    
class Goal(Tile): #Class
    """ 
    Inherits from Tile.
    
    Represents a goal location for a crate to be moved to.
    
    Goal is a type of tile that represents a goal location for a crate. 
    Goal tiles are non-blocking, and the type is represented by 'G'. 
    Goal tiles can either be filled (e.g. contain a crate) or unfilled
    (e.g. empty, with room for one crate). Goal tiles start unfilled,
    and become filled throughout gameplay as the player pushes crates onto them.
    If a goal tile is unfilled, the __str__ and __repr__ methods return 'X'. 
    However, when a goal tile becomes filled, the __str__ and __repr__ methods
    should instead return 'X' to denote that this goal tile is filled. 

    Args:
        Tile (_type_): _description_
    """

    def __init__(self):
        """
        Initalises the Goal class to state that by default, Tiles are not blocking
        A tile is blocking if an entity would not be able to move onto that tile.
        """
        self.blocking = False
        self.filled = False

    def get_type(self) -> str:
        """
        Will get the type of Goal, being 'G' when the tile is unfilled, and 'X'
        when filled.

        Returns:
            The single letter constant corresponding to instantiable subclasses,
            being 'G' when the tile is unfilled, and 'X' when filled.
        """

        while type(self) == Goal:
            if self.blocking is True:
                return GOAL
            elif self.blocking is False:
                return GOAL
    
    def __str__(self) -> str:
        """
        Will get the type of Goal as a string,
        being 'G' when the tile is unfilled, and 'X' when filled.

        Returns:
            str: GOAL is defined in a2_support.py
            str: FILLED_GOAL is defined in a2_support.py
        """

        while type(self) == Goal:
            if self.blocking is True:
                return str(FILLED_GOAL)
            elif self.blocking is False:
                return str(GOAL)
        
    def __repr__(self) -> str:
        """
        Will get the type of Goal as a string,
        being 'G' when the tile is unfilled, and 'X' when filled.

        Returns:
            str: GOAL is defined in a2_support.py
            str: FILLED_GOAL is defined in a2_support.py
        """

        while type(self) == Goal:
            if self.blocking is True:
                return str(FILLED_GOAL)
            elif self.blocking is False:
                return str(GOAL)   

    def is_filled(self) -> bool:
        """
        Returns True only when the goal is filled.

        Returns:
            bool: True only when the goal is filled.
        """

        return self.blocking

    def fill(self) -> None:
        """
        Fills the goal tile.
        """
        self.blocking = True

class Entity: #Abstract Class
    """
    Entities exist on top of the grid (i.e. on top of the tiles), 
    and include the player, all crates, and all potions.
    Entities may or may not be movable.

    Args:
        object (_type_): _description_
    """

    def __init__(self):
        """
        Initalises the Entity class to state that by default, Entities are not movable.
        """
        self.movable = False
        self._type = "Abstract Entity"

    def get_type(self) -> str:
        """
        A string representing the type of this entity. For the abstract 
        Entity class, this method returns the string
        'Abstract Entity'. For instantiable subclasses, this method should return
        the single letter constant corresponding
        to that class.

        Returns:
            'Abstract Entity' for the abstract entity class.
            The single letter constant corresponding to instantiable subclasses.
        """

        return self._type

    def is_movable(self) -> bool:
        """
        Returns True if this entity is movable. By default, entities are not movable.

        Returns:
            bool: True if entity is movable.
            bool: False if entity is not movable.
        """
        return False
    
    def __str__(self) -> str:
        """
        Returns a string representing the type of this entity. In most cases, 
        this will be the same string as would be returned by get_type.

        Returns:
            str: 'Abstract Entity' for the abstract Entity class.
            str: The single letter constant corresponding to instantiable subclasses.
        """
            
        return self._type
        
    def __repr__(self) -> str:
    
        """
        Operates identically to the __str__ method.

        Returns:
            str: 'Abstract Entity' for the abstract Entity class.
            str: The single letter constant corresponding to instantiable subclasses.
        """

        return self._type

class Crate(Entity): #Class
    """
    Crate is a movable entity, represented (in get_type) by the letter 'C'. 
    Crates are constructed with a strength value, which represents the strength 
    a player is required to have in order to move that crate. The string
    representation of a crate should be the string version of its strength 
    value. You may assume that the strength values will always be between
    0 and 9 inclusive.

    Note: blocking players from moving crates that they are not strong enough
    to move should not be handled by the crate class. A crate only needs to be aware 
    of its own strength requirement, and provide an interface through which the model
    class can access that information. 

    Args:
        Entity (_type_): _description_
    """

    def __init__(self, strength: int) -> None:
        """
        Initalises the Crate class and ensures any code from the Entity
        constructor is run, and set this crate's strength value to strength.

        Args:
            strength (int): the given strength value  for the Crate,
            between 0 and 9 inclusive
        """
        self.strength = strength
        self.movable = True

    def get_type(self) -> str:
        """
        The type for CRATE that is defined in a2_support.py

        Returns:
            The single letter constant corresponding to instantiable subclasses.
        """

        return CRATE

    def is_movable(self) -> bool:
        """
        Returns True if this entity is movable. By default, entities are not movable.

        Returns:
            bool: True if entity is movable.
            bool: False if entity is not movable.
        """
        return self.movable
    
    def __str__(self):
        """
        CRATE is a movable entity represented by a single space character.

        Returns:
            str: CRATE is defined in a2_support.py
        """

        if type(self) == Entity:
            return str('Abstract Entity')
        else: 
            return str(self.strength)
        
    def __repr__(self) -> str:
    
        """
        Operates identically to the __str__ method.

        Returns:
            str: CRATE is defined in a2_support.py
        """

        if type(self) == Entity:
            return str('Abstract Entity')
        else: 
            return str(self.strength)
        
    def get_strength(self) -> int:
        """
        The crate's strength value as an integer.
        Returns:
            int: Returns this crate's strength value as an integer.
        """
        return self.strength
        
class Potion(Entity): #Abstract Class
    """
    This is an abstract class which provides a simple interface which all  
    instances of potions must implement. The __init__ method for all potions 
    do not take any arguments besides self. Since this class inherits from Entity, 
    it (along with its subclasses) should also provide all methods available from
    the Entity class. Potions are not movable. An abstract potion is represented 
    by 'Potion' and has no effect.
    Args:
        Entity (_type_): _description_
    """

    def __init__(self):
        """
        Initialises the Potiona class where all potions do not take any arguments
        besides self. Potions are not movable.
        """
        self.movable = False

    def effect(self) -> dict[str, int]:
        """
        Provides a dictionary describing the potion's effect on the player.
        The abstract potion class should just return an empty dictionary, 
        since it has no effect.
        Returns:
            dict[str, int]: A dictionary describing the effect
                            this potion would have on a player.
        """
        return {}

    def get_type(self) -> str:
        """
        The type for potion, being "Potion".

        Returns:
            Potion
        """

        return str("Potion")
    
    def __str__(self) -> str:
        """
        The type for potion as a string, being "Potion".

        Returns:
            str: Potion
        """

        return str("Potion")
    
    def __repr__(self) -> str:
        """
        Operates identically to the __str__ method.

        Returns:
            str: Potion
        """

        return str("Potion")
    
    def is_movable(self) -> bool:
        """
        Returns True if this entity is movable. By default, entities are not movable.
        Potions are not movable.

        Returns:
            bool: False 
        """
        return False

class StrengthPotion(Potion): #Class
    """
    A StrengthPotion is represented by the string 'S' and provides the
    player with an additional 2 strength.

    Args:
        Potion (_type_): _description_
    """

    def effect(self) -> dict[str, int]:
        """
        Provides a dictionary describing the potion's effect on the player.
        StrengthPotion provides the player with an additional 2 strength.
        Returns:
            dict[str, int]: strength: 2
        """
        return {'strength': 2}

    def get_type(self) -> str:
        """
        The type for StrengthPotion, being "S", defined in a2_support.py

        Returns:
             S
            
        """

        return STRENGTH_POTION
    
    def __str__(self) -> str:
        """
        The type for StrengthPotion, being "S", defined in a2_support.py

        Returns:
            str: S
        """

        return str(STRENGTH_POTION)
    
    def __repr__(self) -> str:
        """
        Operates identically to the __str__ method.

        Returns:
            str: S
        """

        return str(STRENGTH_POTION)
    
    def is_movable(self) -> bool:
        """
        Returns True if this entity is movable. By default, entities are not movable.
        Potions are not movable.

        Returns:
            bool: False 
        """
        return False
    
class MovePotion(Potion): #Class
    """
    A MovePotion is represented by the string 'M' and provides the
    player with 5 more moves.

    Args:
        Potion (_type_): _description_
    """

    def effect(self) -> dict[str, int]:
        """
        Provides a dictionary describing the potion's effect on the player.
        MovePotion provides the player with 5 more moves.
        Returns:
            dict[str, int]: moves: 5
        """
        return {'moves': 5}

    def get_type(self) -> str:
        """
        The type for MovePotion, being "M", defined in a2_support.py

        Returns:
             M
        """

        return MOVE_POTION
    
    def __str__(self) -> str:
        """
        The type for MovePotion, being "M", defined in a2_support.py

        Returns:
             M
        """

        return str(MOVE_POTION)
    
    def __repr__(self) -> str:
        """
        Operates identically to the __str__ method.

        Returns:
            str: M
        """

        return str(MOVE_POTION)
    
    def is_movable(self) -> bool:
        """
        Returns True if this entity is movable. By default, entities are not movable.
        Potions are not movable.

        Returns:
            bool: False 
        """
        return False

class FancyPotion(Potion): #Class
    """
    A FancyPotion is represented by the string 'F' and provides the
    player with an additional 2 strength and 2 more moves.

    Args:
        Potion (_type_): _description_
    """

    def effect(self) -> dict[str, int]:
        """
        Provides a dictionary describing the potion's effect on the player.
        FancyPotion provides the player with an additional 2 strength and 2 more moves.
        Returns:
            dict[str, int]: strength: 2, moves: 2
        """
        return {'strength': 2, 'moves': 2}

    def get_type(self) -> str:
        """
        The type for MovePotion, being "F", defined in a2_support.py

        Returns:
             F
        """

        return FANCY_POTION
    
    def __str__(self) -> str:
        """
        The type for MovePotion, being "F", defined in a2_support.py

        Returns:
             F
        """

        return str(FANCY_POTION)
    
    def __repr__(self) -> str:
        """
        Operates identically to the __str__ method.

        Returns:
            str: F
        """

        return str(FANCY_POTION)
    
    def is_movable(self) -> bool:
        """
        Returns True if this entity is movable. By default, entities are not movable.
        Potions are not movable.

        Returns:
            bool: False 
        """
        return False
    
class Player(Entity): #Class
    """Player is a movable entity, represented by the letter 'P'. A player instance
    is constructed with a starting strength and an initial number of moves remaining.
    These two values can change throughout regular gameplay, or through the use of
    potions, via methods provided by the Player class. A player is only movable if they
    have a positive number of moves remaining."""

    def __init__(self, start_strength: int, moves_remaining: int) -> None:
        """
        Initialises the Player class to have a beginning integer 
        of strength and moves remaining.

        Args:
            start_strength (int): _description_
            moves_remaining (int): _description_
        """
        super().__init__()  # Call the constructor of the parent Entity class.
        self._type = PLAYER
        self.strength = start_strength
        self.moves = moves_remaining

        

    def get_strength(self) -> int:
        """
        Provides the strength value of Player

        Returns:
            int: Returns the integer strength value of Player
        """

        return int(self.strength)
    
    def get_moves_remaining(self) -> int:
        """
        Provides the number of moves that Player has remaining

        Returns:
            int: Returns the integer number of moves the Player has remaining
        """

        return int(self.moves)
    
    def add_strength(self, amount: int) -> None:
        """
        Adds an integer strength value to Player's self.strength

        Args:
            amount (int): amount is an integer that is to be
            added to the self.strength of Player 
        """
        self.strength += int(amount)

    def add_moves_remaining(self, amount: int) -> None:
        """
        Adds an integer move value to Player's self.moves

        Args:
            amount (int): amount is an integer that is to be
            added to the self.strength of Player 
        """
        self.moves += int(amount)

    def apply_effect(self, potion_effect: dict[str, int]) -> None:
        """
        Applies the effects described in potion_effect to this player.

        Args:
            potion_effect (dict[str, int]): provides the effect stored 
            in the potion as a dictionary
        """
        if 'strength' in potion_effect:
            self.add_strength(potion_effect['strength'])
        if 'moves' in potion_effect:
            self.add_moves_remaining(potion_effect['moves'])

    def is_movable(self) -> bool:
        """
        Returns True if this entity is movable. By default, entities are not movable.
        Player is not movable.

        Returns:
            bool: False
        """
        return self.moves > 0
    
def convert_maze(game: list[list[str]]) -> tuple[Grid, Entities, Position]: 
    """
    Converts the simple format of the maze representation into a more 
    sophisticated representation with tiles and entities. 

    Args:
        game (list[list[str]]): A list representing the Sokoban maze, 
        where each string character represents a tile or entity at that location.


    Returns:
        tuple[Grid, Entities, Position]: Returns a tuple containing these three 
        structures (in order).
    """

    grid = []  # Initialise an empty list to store the grid.
    entities = {}  # Initialise an empty dictionary to store entities' positions.
    player_position = None

    for row_index, row in enumerate(game):
        grid_row = []  # Initialise an empty list for the current row in the grid.
        
        for column_position, char in enumerate(row):
            if char == WALL:
                grid_row.append(Wall())  
            elif char == FLOOR:
                grid_row.append(Floor())  
            elif char == GOAL:
                grid_row.append(Goal())
                
            # Put potions in dictionary
            elif char == STRENGTH_POTION:
                entities[(row_index, column_position)] = StrengthPotion()
            elif char == MOVE_POTION:
                entities[(row_index, column_position)] = MovePotion()
            elif char == FANCY_POTION:
                entities[(row_index, column_position)] = FancyPotion()


            elif char.isdigit(): # For digits between 0 and 9 inclusive, crate strength 
                entities[(row_index, column_position)] = Crate(int(char))
                grid_row.append(Floor()) 

            elif char == PLAYER:
                player_position = (row_index, column_position) 
                grid_row.append(Floor())  
        
        grid.append(grid_row)

    return grid, entities, player_position

class SokobanModel:
    """
    A class responsible for maintaining the game state, and applying game logic. 
    """

    def __init__(self, maze_file: str) -> None:
        """
        Read the given maze file from a2_support.py), 
        call the convert_maze function to get representations for the maze,
        non-player entities, and player position. Construct a player 
        instance with the 8 player stats described in the maze file.
        It is assumed that the maze file will not contain any goals
        that are already filled.
        Args:
            maze_file (str): _description_
        """
        def_maze, player_stats = read_file(maze_file)
        self.maze, self.entities, self.player_position = convert_maze(def_maze)
        self.player = Player(*player_stats)
        # self._crate_position = crate_position

    def get_maze(self) -> Grid:
        """
            Returns the maze representation (list of lists of Tile instances).

            Returns: The sokoban board

            Grid: _description_
            """

        return self.maze
    
    def get_entities(self) -> Entities:
        """
        Returns the dicitonary mapping positions to non-player entities.

        Returns:
            Entities: _description_
        """

        return self.entities
    
    def get_player_position(self) -> tuple[int, int]:
        """
        Returns the player's current position.
        Returns:
            tuple[int, int]: _description_
        """

        return self.player_position
    
    def get_player_moves_remaining(self) -> int: 
        """
        Returns the number of moves the player has remaining.

        Returns:
            int: _description_
        """

        return self.player.get_moves_remaining()
    
    def get_player_strength(self) -> int:
        """
        Returns the player's current strength.

        Returns:
            int: _description_
        """
        
        return self.player.get_strength()
    
    def crate_in_goal(self, crate_posx, crate_posy) -> None:
        """ Checks if the crate is in the goal.
        
        ReturnS:
            bool: _description_
        
        """
        
        if self.maze[crate_posx][crate_posy].get_type() == GOAL:
            self.maze[crate_posx][crate_posy].fill()
            del self.entities[(crate_posx, crate_posy)]
        
        
    
    def attempt_move(self, direction: str) -> bool:
        """attempt_move _summary_

        _extended_summary_

        Args:
            direction (str): _description_

        Returns:
            bool: _description_
        """

        entities = self.get_entities()
        positon = self.get_player_position()
        # crate_position = {}
        # for i, row in enumerate(self._maze):
        #     for j, cell in enumerate(row):
        #         if cell.get_type() == GOAL:
        #             crate_position[(i, j)] = cell

        if direction not in DIRECTION_DELTAS:
            return False
        positionx = self.player_position[0]
        positiony = self.player_position[1]
        
        new_position_x = positionx + DIRECTION_DELTAS[direction][0]
        new_position_y = positiony + DIRECTION_DELTAS[direction][1]
        new_c_posx = new_position_x + DIRECTION_DELTAS[direction][0]
        new_c_posy = new_position_y + DIRECTION_DELTAS[direction][1]
        
        if not (0 <= new_position_x < len(self.maze) and 0 <= new_position_y < len(self.maze[0])): # Check if new position is blocked, invalid
            return False
        
        if self.maze[new_position_x][new_position_y].is_blocking(): # Check if new position is blocked.
            return False
        if (new_position_x, new_position_y) in entities and \
            entities[(new_position_x, new_position_y)].get_type() in [MOVE_POTION, STRENGTH_POTION, FANCY_POTION]:
            self.player.apply_effect(self.entities[(new_position_x, new_position_y)].effect()) # Apply potion effect
            del entities[(new_position_x, new_position_y)] # Delete potion from entities
            self.player_position = (new_position_x, new_position_y) # Update player position
            self.player.add_moves_remaining(-1)
            # Check for crate strength
            # if crate.strength < player.strength:
            #     pass
        elif (new_position_x, new_position_y) in entities and entities[(new_position_x, new_position_y)].is_movable():
            crate_strength = entities[(new_position_x, new_position_y)].get_strength()
            if crate_strength > self.get_player_strength():
                return False
            elif not self.maze[new_c_posx][new_c_posy].is_blocking():
                    del entities[(new_position_x, new_position_y)]
                    entities[(new_c_posx, new_c_posy)] = Crate(crate_strength)
                    self.player_position = (new_position_x, new_position_y)
                    self.player.add_moves_remaining(-1)
                    self.crate_in_goal(new_c_posx, new_c_posy)
                    return True
                # Check for filled goal
                
            else:
                return False
        else:
            self.player_position = (new_position_x, new_position_y)
            self.player.add_moves_remaining(-1)
            return True

        return False

    
    def has_won(self) -> bool: 
        """
        The game has been won if all goals are filled, or equivalently
        {since the number of goals is always equal to the number of crates),
        there are no more crates on the grid.

        Returns:
            bool: Returns True only when the game has been won, else False
        """
        goal_position = {}
        for num, row in enumerate(self.maze):
            for num2, cell in enumerate(row):
                if cell.get_type() == GOAL:
                    goal_position[(num, num2)] = cell
        
        for goal in goal_position:
            if goal_position[goal].is_filled() is False:
                return False
        return True
    
    def is_game_lost(self) -> bool:
        """
        Check if the game has been lost based on your game logic.
        For example, you can check if the player has run out of moves.
        
        Returns:
            bool: True if the game is lost, False otherwise.
        """
        # Implement your game loss condition here
        # For example, check if the player has run out of moves
        return self.get_player_moves_remaining() <= 0 #msafnkdasd,nasjfmnsakfmnsajkdasjkdmanszd ask
    
class Sokoban:
    """
    _extended_summary_
    """

    def __init__(self, maze_file: str) -> None:
        """
        This method should construct an instance of the SokobanModel class using the
        provided maze_file, as well as an instance of the SokobanView class.
        Args:
            maze_file (str): _description_
        """
        self.model = SokobanModel(maze_file)
        self.view = SokobanView()

    def display(self) -> None:
        """
        This method should call the display_game and display_stats methods on the 
        instance of the SokobanView class. The arguments given should be based on 
        the state of the game as defined by the SokobanModel instance.
        """
        game_state = {
            'maze': self.model.get_maze(),
            'entities': self.model.get_entities(),
            'player_moves_remaining': self.model.get_player_moves_remaining(),
            'player_strength': self.model.get_player_strength(),
        }
        self.view.display_game(
            game_state['maze'],
            game_state['entities'],
            self.model.get_player_position()
        )
        self.view.display_stats(
            game_state['player_moves_remaining'],
            game_state['player_strength']
        )

    def play_game(self) -> None: 
        """
        This method runs the main game loop and implements the specified behavior.
        While the game is still going (i.e. the function has not returned), repeat:
        1. If the game is won, display game state and print 'You won!', and return.
        2. If the game has been lost, display the message 'You lost!', and return.
        3. Display the current game state.
        4. Prompt the user for a move with the prompt 'Enter move: '.
        5. If the move is 'q', return, else tell the model to attempt the given move.
        6. If the move was invalid, display the message 'Invalid move\n'.
        """

        while True: 
            if self.model.has_won():
                self.display()
                print("You won!")
                return

            if self.model.is_game_lost():
                print("You lost!")
                return

            self.display()

            move = input("Enter move: ")

            if move == 'q':
                return
            elif not self.model.attempt_move(move):
                    print("Invalid move\n")

def main():
    # uncomment the lines below once you've written your Sokoban class
    game = Sokoban('maze_files/maze1.txt')
    game.play_game()
    pass

if __name__ == '__main__':
    main()
