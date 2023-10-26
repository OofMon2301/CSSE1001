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
        AbstractGrid (class): A class that represents the grid of the game.
    """

    def __init__(
        self,
        master: tk.Frame | tk.Tk,
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs,
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
        super().__init__(master, dimensions=(8, 7), size=(450, 450))

        self._master = master
        self._size = size
        self._dimensions = dimensions
        self.set_dimensions(dimensions)
        self._image_cache = {}

    def image_processing(self) -> None:
        """image_processing Processes the images."""

        images = {
            "$": "images/$.png",
            "C": "images/C.png",
            "F": "images/F.png",
            "G": "images/G.png",
            "M": "images/M.png",
            "P": "images/P.png",
            "S": "images/S.png",
            "W": "images/W.png",
            "X": "images/X.png",
            "Floor": "images/Floor.png",
        }
        real_image = {}

        # Make the image using get_image and place in real_image
        for key in images:
            real_image[key] = get_image(
                images[key], self.get_cell_size(), self._image_cache
            )
        return real_image

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
        self._game = game
        self._entities = entities
        self._player_position = player_position

        # Basic Grid

        real_image = self.image_processing()

        for row_idx, row in enumerate(self._game):
            for col_idx, col in enumerate(row):
                if str(self._game[row_idx][col_idx]) in real_image:
                    self.create_image(
                        self.get_midpoint(position=(row_idx, col_idx)),
                        image=real_image[str(self._game[row_idx][col_idx])],
                    )
                else:
                    self.create_image(
                        self.get_midpoint(position=(row_idx, col_idx)),
                        image=real_image["Floor"],
                    )

        for key in self._entities:
            if str(self._entities[key]) in real_image:
                self.create_image(
                    self.get_midpoint(position=key),
                    image=real_image[str(self._entities[key])],
                )
            else:
                self.create_image(
                    self.get_midpoint(position=key),
                    image=real_image["C"],
                )

                self.annotate_position(
                    key, self._entities[key].get_strength(), font=TITLE_FONT
                )

        self.create_image(
            self.get_midpoint(position=(self._player_position)),
            image=real_image["P"],
        )


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
        super().__init__(
            master,
            dimensions=(3, 3),
            size=(MAZE_SIZE + SHOP_WIDTH, STATS_HEIGHT),
        )
        self._master = master
        self._dimensions = (3, 3)
        self._size = (650, 75)
        self.set_dimensions(self._dimensions)

        self.annotate_position((0, 1), "Player Stats", TITLE_FONT)

        # Stats for the moves, strength, and money

        self.label = "Moves remaining:", "Strength:", "Money:"

        for row in range(3):
            self.annotate_position(
                (1, row),
                self.label[row],
            )

        # Values for the stats
        self.draw_stats(12, 1, 0)

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
        self.clear()

        self.annotate_position((0, 1), "Player Stats", TITLE_FONT)

        # Stats for the moves, strength, and money
        for row in range(3):
            self.annotate_position(
                (1, row),
                self.label[row],
            )

        stats = [moves_remaining, strength, f"${money}"]
        # Iterate through the stats
        for row in range(3):
            self.annotate_position(
                (2, row),
                stats[row],
            )


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
        a title label

        Args:
            master (tk.Tk | tk.Frame): Frame or Tk object
        """
        super().__init__(master)
        title_label = tk.Label(self, text="Shop", font=(TITLE_FONT))
        title_label.pack(side=tk.TOP, padx=65)

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
        frame = tk.Frame(self)

        potion = tk.Label(frame, text=f"{item}: ${amount}")
        potion.pack(side=tk.LEFT)

        button = tk.Button(frame, text="Buy", command=callback)
        button.pack(side=tk.LEFT)

        frame.pack(side=tk.TOP)


class FancySokobanView:
    """FancySokobanView A view for the game.

    The FancySokobanView is a class. It is
    responsible for generating a graphical view of the game and handling user
    input (e.g. all tiles and entities, including the player).

    The FancySokobanView class provides a wrapper around the smaller
    GUI components you have just built, and provides methods through
    which the controller can update these components.

    Args:
        FancySokobanView (class): A class that represents the grid of the game.
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
        self._image_cache = {}
        self._dimensions = dimensions
        self._size = size
        self._master = master

        image = get_image(
            "images/banner.png",
            (MAZE_SIZE + SHOP_WIDTH, BANNER_HEIGHT),
            self._image_cache,
        )

        banner_label = tk.Label(
            master=master,
            image=image,
            width=MAZE_SIZE + SHOP_WIDTH,
            height=BANNER_HEIGHT,
        )
        banner_label.pack(side=tk.TOP)

        master.title("Extra Fancy Sokoban")

        # Set new Frame for Game and Shop to sit together
        self.game_shop_frame = tk.Frame(
            master, width=MAZE_SIZE + SHOP_WIDTH, height=MAZE_SIZE
        )

        self._game_view = FancyGameView(self.game_shop_frame, dimensions, size)
        self._game_view.pack(side=tk.LEFT)

        self._shop_view = Shop(self.game_shop_frame)
        self._shop_view.pack(side=tk.LEFT)

        self.game_shop_frame.pack(side=tk.TOP)

        self._stats_view = FancyStatsView(master)
        self._stats_view.pack(side=tk.TOP)

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
        self._game_view.delete(tk.ALL)
        self._game_view.display(maze, entities, player_position)

        self._game_view.update()

    def display_stats(self, moves: int, strength: int, money: int) -> None:
        """display_stats Displays the stats of the player.

        This method clears and redraws the stats view.

        Args:
            moves (int): The number of moves remaining
            strength (int): The strength of the player
            money (int): The amount of money the player has
        """
        self._stats_view.clear()
        self._stats_view.draw_stats(moves, strength, money)

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
        ITEMS = {
            "S": "Strength Potion",
            "M": "Move Potion",
            "F": "Fancy Potion",
        }

        for item in shop_items:
            price = shop_items[item]
            # Create the button callback
            btn_callback = lambda x=item: button_callback(x)

            self._shop_view.create_buyable_item(
                ITEMS[item], price, btn_callback
            )


class ExtraFancySokoban:
    """The overall controller class for the game.

    ExtraFancySokoban is a class. It is responsible for
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
        self._root = root
        self._maze_file = maze_file

        # Gather all data from the model
        dimensions, player_position, entities, maze = data_gathering(maze_file)
        self._model = SokobanModel(maze_file)

        # Call the view
        self._view = FancySokobanView(root, dimensions, (MAZE_SIZE, MAZE_SIZE))

        # Run the graphics
        self._view.display_game(maze, entities, player_position)

        # Bind the keypress events to the relevant handler
        root.bind("<KeyPress>", self.handle_keypress)

        self._view.create_shop_items(
            self._model.get_shop_items(), self.item_callback
        )

    def item_callback(self, item_id: str) -> None:
        if self._model.attempt_purchase(item_id):
            self.redraw()
        else:
            messagebox.showerror("Error", "You do not have enough money.")

    def redraw(self) -> None:
        """redraw Redraws the display (stats and game view) to show the
        current game state.
        """

        self._view.display_game(
            self._model.get_maze(),
            self._model.get_entities(),
            self._model.get_player_position(),
        )
        self._view.display_stats(
            self._model.get_player_moves_remaining(),
            self._model.get_player_strength(),
            self._model.get_player_money(),
        )

    def win_state(self) -> None:
        """win_state Determine if there is a win or a loss.

        This method determines if there is a win or a loss by checking if
        the game has been won or lost. If the game has been won or lost,
        this method should cause a messagebox to display informing the user
        of the outcome and asking if they would like to play again.
        If the user selects yes, the game should be reset (i.e. reset the
        model and then redraw the view). If the user selects no, the program
        should terminate gracefully.
        """
        entities = self._model.get_entities()

        # Win State
        win_state = True
        for ind_entity in entities:
            if str(entities[ind_entity]) in str([1, 2, 3, 4, 5, 6, 7, 8, 9]):
                win_state = False
                break
        if win_state is True:
            if (
                messagebox.askquestion("Game Over", "You won! Play again?")
                == "yes"
            ):
                # Reset the game
                self._model = SokobanModel(self._maze_file)
                self.redraw()
            else:
                self._root.quit()

        # Lose state
        elif self._model.get_player_moves_remaining() <= 0:
            # Display a message box
            if (
                messagebox.askquestion("Game Over", "You lost! Play again?")
                == "yes"
            ):
                # Reset the game
                self._model = SokobanModel(self._maze_file)
                self.redraw()
            else:
                self._root.quit()

                # self._model.has_won()

    def handle_keypress(self, event: tk.Event) -> None:
        """handle_keypress Handles the keypress events.

        This method handles the keypress events by calling the appropriate
        methods to update the game state and then redrawing the display to
        show the updated game state.

        An event handler to be called when a keypress event occurs.
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
        # When a key is pressed, check what key is pressed first
        # If it is a movement key, move the player

        if event.char in [UP, DOWN, LEFT, RIGHT, "u"]:
            # Attempt to move the player
            self._model.attempt_move(event.char)
            if True:
                # Redraw the display
                self.redraw()
                # Check for win
                self.win_state()
        else:
            print(f"Please press a valid key. \n")
            return


def data_gathering(maze_file: str) -> None:
    """data_gathering Gathers all the data from the model.

    This method gathers all the data from the model and stores it in
    instance attributes.
    """

    model = SokobanModel(maze_file)
    dimensions = model.get_dimensions()
    player_position = model.get_player_position()
    entities = model.get_entities()
    maze = model.get_maze()

    return dimensions, player_position, entities, maze


def play_game(root: tk.Tk, maze_file: str) -> None:
    """Play the game."""

    ExtraFancySokoban(root, maze_file)

    root.mainloop()


def main() -> None:
    """The main function.

    Should construct the root tk.Tk instance and call the play_game function
    passing in the newly created root instance and the path to any map that
    you want to play (e.g. 'maze files/maze1.txt')
    """
    root = tk.Tk()

    root.geometry("650x600")

    maze_file = filedialog.askopenfilename(
        initialdir="/maze_files", title="Select Maze File"
    )

    if not maze_file:
        messagebox.showerror("Error", "No file selected. Exiting program.")
        exit()
    play_game(root, maze_file)


if __name__ == "__main__":
    main()
