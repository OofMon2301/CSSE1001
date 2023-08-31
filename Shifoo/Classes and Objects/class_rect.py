from __future__ import annotations

"""
Define a Rectangle class with a constructor that takes (in this order) an integer tuple encoding the rectangle's top-left corner, the rectangle's integer width, and the rectangle's integer height
"""


class Rectangle:
    def __init__(self, lcorner, width, height) -> None:
        self.lcorner = lcorner
        self.width = width
        self.height = height

    def get_bottom_right(self) -> tuple(int):
        """get_bottom_right Gets the bottom right coordinates of the rectangle"""
        return (self.lcorner[0] + self.width, self.lcorner[1] + self.height)

    def move(self, new_corner: tuple(int)) -> None:
        # Move to make the new corner the top left corner but leave the width and height unchanged
        self.lcorner = new_corner

    def resize(self, new_width: int, new_height: int) -> None:
        # Changes the width and height of the rectangle but keep the position of top left corner the same.
        self.width = new_width
        self.height = new_height
        return

    def __str__(self) -> str:
        # return pair of numbers (top right and bottom left corners) in brackets
        return f"({self.lcorner}, {self.get_bottom_right()})"
