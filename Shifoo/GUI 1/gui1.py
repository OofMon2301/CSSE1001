import tkinter as tk


def pressed():
    """
    Button callback function (command).

    You may alter what this function does if you wish, but you must not rename
    or delete it.

    """
    print("Button Pressed!")


def create_layout(frame: tk.Frame) -> None:
    """
    Add two buttons to the frame.

    Both buttons should have the callback (command) pressed, and they should
    have the labels "Button1" and "Button2".

    The layout in the frame after running this function will be:
      +-----------------------+
      |[Button1][Button2]     |
      +-----------------------+

    Parameters:
        frame : The frame to create the two buttons in.

    """
    button1 = tk.Button(frame, text="Button1", command=pressed)
    button2 = tk.Button(frame, text="Button2", command=pressed)
    button1.pack(side=tk.LEFT)
    button2.pack(side=tk.LEFT)
