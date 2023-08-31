import tkinter as tk


def pressed():
    """
    Button callback function (command).

    You may alter what this function does if you wish, but you must not rename
    or delete it.

    """
    print("Button Pressed!")


def create_layout(frame: tk.Frame) -> None:
    """docstring for create_layout"""
    button1 = tk.Button(frame, text="Button1", command=pressed)
    button1.pack(side=tk.LEFT, padx=20)

    button2_frame = tk.Frame(frame)
    button2_frame.pack(side=tk.LEFT, fill=tk.Y)

    button2 = tk.Button(button2_frame, text="Button2", command=pressed)
    button2.pack(side=tk.TOP, fill=tk.X, padx=20, pady=20)\
    
    
    
