from __future__ import annotations


class Shape:
    """
    A representation of a shape.

    """

    def __init__(self, origin: tuple[int, int] = (0, 0)) -> None:
        """Construct a shape object

        Parameters:
            origin: origin of the shape

        """

        self.origin = origin

    def area(self) -> int:
        """
        Return the area of the shape.

        """
        raise NotImplementedError()

    def vertices(self) -> list[tuple[int, int]]:
        """
        Return the vertices of the shape in any order.


        """
        raise NotImplementedError()


class Square(Shape):
    """A Square object"""

    def __init__(self, side_length: int, origin: tuple[int, int] = (0, 0)) -> None:
        """
        Construct a square object

        Parameters:
            side_length: Side length of the square
            origin: Coordinate of top-left corner of square

        """

        super().__init__(origin=origin)
        self.side_length = side_length

    def area(self) -> int:
        """
        Return the area of the shape.

        """
        return self.side_length * self.side_length

    def vertices(self) -> list[tuple[int, int]]:
        """
        Return the vertices of the shape.  This list has no order.

        """
        x, y = self.origin

        return [
            (x, y),
            (x, y + self.side_length),
            (x + self.side_length, y + self.side_length),
            (x + self.side_length, y),
        ]


class RightAngledTriangle(Shape):
    def __init__(self, points: list[tuple[int, int]]) -> None:
        """
        Construct a right angle triangle object

        Parameters:
            A list of points forming the triangle

        """
        super().__init__(origin=points[0])
        self.points = points

    def area(self) -> int:
        """
        Return the area of the shape.

        """
        for i in range(3):
            if self.points[i][0] != 0 and self.points[i][1] != 0:
                base = abs(self.points[i][0] - self.points[(i + 1) % 3][0])
                height = abs(self.points[i][1] - self.points[0][1])
                break
        return int(base * height) // 2

    def vertices(self) -> list[tuple[int, int]]:
        """
        Return the vertices of the shape.  This list has no order.

        """
        return self.points


class Rectangle(Shape):
    def __init__(
        self, width: int, height: int, origin: tuple[int, int] = (0, 0)
    ) -> None:
        """
        Construct a rectangle object

        Parameters:
            width: Width of the rectangle
            height: Height of the rectangle
            origin: Coordinate of top-left corner of rectangle

        """
        super().__init__(origin=origin)
        self.width = width
        self.height = height

    def vertices(self) -> list[tuple[int, int]]:
        x, y = self.origin
        return [
            (x, y),
            (x, y + self.height),
            (x + self.width, y + self.height),
            (x + self.width, y),
        ]

    def area(self) -> int:
        return self.width * self.height


def total_area(shapes: list[Shape]) -> float:
    """
    Return the total area of the given list of shapes.

    Parameters:
        shapes: The list of shapes to sum the area for.

    """
    area = 0.0

    for shape in shapes:
        area += shape.area()

    return area


def outer_bounds(shapes: list[Shape]) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Return the outer bounds of the given list of shapes.

    Parameters:
        shapes: The list of shapes to return the outer bounds for.

    Note:
        The first element of the tuple is the top-left corner of a rectangle
        which could enclose every shape in the given list.
        The second element of the tuple is the bottom-right corner of that same
        rectangle.

        The top-left corner of the rectangle will be, at minimum, (0, 0).

    """
    vertices = []

    for shape in shapes:
        for vertex in shape.vertices():
            vertices.append(vertex)

    top_left_x = 0
    top_left_y = 0
    bottom_right_x = 0
    bottom_right_y = 0

    for x, y in vertices:
        if x < top_left_x:
            top_left_x = x
        elif x > bottom_right_x:
            bottom_right_x = x

        if y < top_left_y:
            top_left_y = y
        elif y > bottom_right_y:
            bottom_right_y = y

    return (top_left_x, top_left_y), (bottom_right_x, bottom_right_y)
