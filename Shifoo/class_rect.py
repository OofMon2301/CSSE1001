from __future__ import annotations

"""
Define a Rectangle class with a constructor that takes (in this order) an integer tuple encoding the rectangle's top-left corner, the rectangle's integer width, and the rectangle's integer height
"""


class Rectangle:
    
    
    def get_bottom_right(self) -> tuple(int):
        pass
    
    
    def move(self, new_corner: tuple(int)) -> None:
        pass
    
    
    def resize(self, new_width: int, new_height: int) -> None:
        pass

    
    def __str__(self) -> str:
        pass