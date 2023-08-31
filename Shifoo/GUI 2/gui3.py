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
    Add four buttons to the frame in the given format.

    Both buttons should have the callback (command) pressed, and they should
    have the labels "Button1" through "Button4".

    The layout in the frame after running this function will be:
        +---------------------------------------+
        |                                       |
        |  [Button1]                            |
        |               [Button3]    [Button4]  |
        |  [Button2]                            |
        |                                       |
        +---------------------------------------+

    Parameters:
            frame (tk.Frame): The frame to create the two buttons in.

    """
    frameleft = tk.Frame(frame)
    frameleft.pack(fill=tk.BOTH)

    button1 = tk.Button(frameleft, text="Button1", command=pressed)
    button1.pack(side=tk.TOP, padx=20, pady=20, expand=True)

    button2 = tk.Button(frameleft, text="Button2", command=pressed)
    button2.pack(side=tk.TOP, padx=20, pady=20, expand=True)

    button3 = tk.Button(frame, text="Button3", command=pressed)
    button3.pack(side=tk.LEFT, padx=20, pady=20, expand=True)

    button4 = tk.Button(frame, text="Button4", command=pressed)
    button4.pack(side=tk.LEFT, padx=20, pady=20, expand=True)
