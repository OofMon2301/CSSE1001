import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Union
from model import SokobanModel, Tile, Entity
from a2_support import *
from a3_support import *

# Write your classes and functions here


class FancyGameView(AbstractGrid):
    """FancyGameView generates a graphical view of the game.

    FancyGameView is a subclass of AbstractGrid. It is responsible for
    generating a graphical view of the game and handling user input
    (e.g. all tiles and entities, including the player).

    Args:
        AbstractGrid (_type_): A class that represents the grid of the game.
    """

    def __init__(
        self,
        master: tk.Frame | tk.Tk,
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs
    ) -> None:
        """__init__ An initialiser for FancyGameView.

        This initialiser sets up the FancyGameView to be an AbstractGrid with
        the appropriate dimensions and size, and creates an instance attribute
        of an empty dictionary to be used as an image cache.

        Args:
            master (tk.Frame | tk.Tk): Frame or Tk object
            dimensions (tuple[int, int]): dimensions of the grid
            size (tuple[int, int]): coordinates of the grid
        """
        super().__init__(master, dimensions, size, **kwargs)
        self._image_cache = {}

    def display(
        self, game: Grid, entities: Entities, player_position: Position
    ) -> None:
        """display Displays the game and entities.

        This method displays the game and entities by iterating through the
        grid and entities and calling the appropriate methods to display them.
        Clears the game view, then creates (on the FancyGameView instance
        itself) the images for the tiles and entities. If an entity is at a
        specific location, you may assume there is a FLOOR tile undeneath.
        If an entity is at a position, the tile image should be rendered
        beneath the entity image.

        Args:
            game (Grid): The grid of the game
            entities (list[Entity]): The list of entities in the game
        """
        # Clears the game view and then updates the game view
        self.clear()
        # If there is a tile at a specific location, create the image for it

        pass  # Write your code here


class FancyStatsView(AbstractGrid):
    """FancyStatsView A Fancy view of the stats of the player.

    It is a grid with 3 rows and 3 columns. The top row displays the text
    'Player Stats' in a bold font in the second column. The second row displays
    titles for the stats, and the third row displays the values for those stats.
    The FancyStatsView should span the entire width of the game and shop
    combined.

    Args:
        AbstractGrid (class): a class that represents the grid of the game
    """

    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        """__init__ An initialiser for FancyStatsView.

        This initialiser sets up the FancyStatsView to be an AbstractGrid with
        the appropriate dimensions and size.

        Args:
            master (tk.Tk | tk.Frame): Frame or Tk object
        """
        super().__init__(master, (3, 3), (0, 0))

    def draw_stats(
        self, moves_remaining: int, strength: int, money: int
    ) -> None:
        """draw_stats Draws the stats of the player.

        This method draws the stats of the player by iterating through the
        stats and displaying them in the appropriate locations.
        Clears the FancyStatsView, then creates the labels for the stats.

        Args:
            moves_remaining (int): The number of moves remaining
            strength (int): The strength of the player
            money (int): The amount of money the player has
        """
        pass


class Shop(tk.Frame):
    """Shop A shop for the player to buy items.

    The Shop is a frame displaying relevant information and buttons for all
    the buyable items in the game (see the get shop items
    method in SokobanModel). The Shop should contain a title at the top and
    a frame for each buyable item (each potion).

    Each item's frame should contain the following widgets,
    packed left to right:

    - A label with the item's name and the cost
    - A button to buy the item. The callback for these buttons must be
    created in the controller (see ExtraFancySokoban) and passed to the
    Shop when calling create_buyable_item.

    Args:
        tk (class): a class that represents the grid of the game
    """

    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        """__init__ An initialiser for Shop.

        This initialiser sets up the shop to act like a tk.Frame and to have
        a title label at the top in bold font.

        Args:
            master (tk.Tk | tk.Frame): Frame or Tk object
        """
        # Crate shop tk.Frame
        super().__init__(master)
        title_label = tk.Label(master, text="Shop", font=(FONT))
        title_label.pack(side="top", pady=10)

    def create_buyable_item(
        self, item: str, amount: int, callback: Callable[[], None]
    ) -> None:
        """create_buyable_item Creates a buyable item.

        This method creates a buyable item by creating a frame for it and
        adding a label with the item's name and cost, and a button to buy the
        item. The callback for the button is passed in as a parameter.
        Create a new item in this shop. That is, this method creates a new
        frame within the shop frame and then creates a label and button within
        that child frame. The button should be bound to the provided callback.

        Args:
            item (str): The name of the item
            amount (int): The cost of the item
            callback (Callable[[], None]): The callback for the button
        """
        pass


class FancySokobanView:
    """FancySokobanView A view for the game.

    The FancySokobanView is a subclass of AbstractSokobanView. It is
    responsible for generating a graphical view of the game and handling user
    input (e.g. all tiles and entities, including the player).

    The FancySokobanView class provides a wrapper around the smaller
    GUI components you have just built, and provides methods through
    which the controller can update these components.

    Args:
        AbstractSokobanView (_type_): A class that represents the grid of the game.
    """

    def __init__(
        self, master: tk.Tk, dimensions: tuple[int, int], size: tuple[int, int]
    ) -> None:
        """__init__ An initialiser for FancySokobanView.

        This initialiser sets up a new FancySokobanView instance.

        Args:
            master (tk.Tk | tk.Frame): Frame or Tk object
            dimensions (tuple[int, int]): dimensions of the grid
            size (tuple[int, int]): coordinates of the grid
        """
        # Sets up the title banner
        title_banner = tk.Frame(master)
        # Gets the banner image and put on top of the window
        get_image(
            "Assignments/a3/images/banner.png",
            (MAZE_SIZE + SHOP_WIDTH, BANNER_HEIGHT),
        )

        title_banner.pack(side="top", fill=tk.X)
        master.title("Extra Fancy Sokoban")

        # Sets up the game view
        game_view = FancyGameView(master, dimensions, size)
        game_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Sets up the stats view
        stats_view = FancyStatsView(master)
        stats_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Sets up the shop
        shop = Shop(master)
        shop.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Sets the title on the window
        master.title("Sokoban")

    def display_game(
        self, maze: Grid, entities: Entities, player_position: Position
    ) -> None:
        """display_game Displays the game and entities.

        This method clears and redraws the game view.

        Args:
            maze (Grid): The grid of the game
            entities (list[Entity]): The list of entities in the game
            player_position (Position): The position of the player
        """
        pass

    def display_stats(self, moves: int, strength: int, money: int) -> None:
        """display_stats Displays the stats of the player.

        This method clears and redraws the stats view.

        Args:
            moves (int): The number of moves remaining
            strength (int): The strength of the player
            money (int): The amount of money the player has
        """
        pass

    def create_shop_items(
        self,
        shop_items: dict[str, int],
        button_callback: Callable[[str], None] | None = None,
    ) -> None:
        """create_shop_items Creates the items in the shop.

        Creates all the buyable items in the shop. shop items maps item id's
        (result of calling get type on the item entity) to price. For each of
        these items, the callback given to create buyable item in Shop should
        be a function which requires no positional arguments and calls button
        callback with the item id as an argument.

        Args:
            shop_items (dict[str, int]): The items in the shop
            button_callback (Callable[[str], None], optional): The callback for
            the button. Defaults to None.
        """
        pass


class ExtraFancySokoban:
    """The overall controller class for the game.

    ExtraFancySokoban is a subclass of AbstractSokoban. It is responsible for
    handling the game logic and for updating the view when necessary.
    """

    def __init__(self, root: tk.Tk, maze_file: str) -> None:
        """__init__ Sets up the ExtraFancySokoban Instance.

        This includes creating instances of SokobanModel and SokobanView,
        creating the shop items, binding keypress events to the relevant
        handler, and then redrawing the display to show the initial game state.

        1. Take an item id as a parameter and buy the item if the player has
        2. Attempt to buy the item
        3. Tells the entire game to update itself
        Args:
            root (tk.Tk): Tk object
            maze_file (str): the directory of the maze file
        """
        pass

    def redraw(self) -> None:
        """redraw Redraws the display to show the current game state."""
        pass

    def handle_keypress(self, event: tk.Event) -> None:
        """handle_keypress Handles the keypress events.

        This method handles the keypress events by calling the appropriate
        methods to update the game state and then redrawing the display to
        show the updated game state.

        An event handler to be called whena keypress event occurs.
        Should tell the model to attempt the move as per the key pressed,and
        then redraw the view. If the game has been won or lost after the move,
        this method should cause a messagebox to display informing the user of
        the outcome and asking if theywould like to play again. If the user
        selects yes, the game should be reset(i.e. reset the model and then
        redraw the view). If the user selects no, the program should
        terminate gracefully.

        Args:
            event (tk.Event): The keypress event
        """
        pass


def play_game() -> None:
    """Play the game."""
    # Create the root Tk instance
    root = tk.Tk()
    # Find dimensions of maze and entity positions
    dimensions, entities = read_file("Assignments/a3/maze_files/maze1.txt")

    # Write your code here


def main() -> None:
    """The main function.

    Should construct the root tk.Tk instance and call the play_game function
    passing in the newly created root instance and the path to any map that
    you want to play (e.g. 'maze files/maze1.txt')
    """
    # Read file
    # Get the dimensions from model.py
    dimensions = SokobanModel(
        "Assignments/a3/maze_files/maze1.txt"
    ).get_dimensions()
    # Create the root Tk instance
    root = tk.Tk()

    # Create the game view
    FancySokobanView(root, dimensions, (MAZE_SIZE, MAZE_SIZE))
    root.mainloop()
    # Play the game
    play_game()


if __name__ == "__main__":
    main()
