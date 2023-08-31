from __future__ import annotations
import math

EPSILON = 1e-5


class Point(object):
    """A 2D point in the cartesian plane"""

    def __init__(self, x: float, y: float) -> None:
        """
        Construct a 2D point object.

        Parameters:
            x: x coordinate in the 2D cartesian plane
            y: y coordinate in the 2D cartesian plane
        """

        self._x = x
        self._y = y

    def __repr__(self):
        return "Point({}, {})".format(self._x, self._y)

    def dist_to_point(self, other: Point) -> float:
        """
        Examples:
        >>> x, y = Point(0, 0), Point(3, 4)
        >>> x.dist_to_point(y)
        5
        """
        return math.sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)

    def is_near(self, other: Point) -> bool:
        """
        Examples:
        >>> x, y = Point(0, 0), Point(3, 4)
        >>> x.is_near(y)
        False
        >>> x, y = Point(0, 0), Point(10**-6, 10**-6)
        True
        """
        if self.dist_to_point(other) < EPSILON:
            return True
        else:
            return False

    def add_point(self, other: Point) -> None:
        """
        Examples:
        >>> x, y = Point(1, 2), Point(3, 4)
        >>> x.add_point(y)
        >>> x
        Point(4, 6)
        """
        self._x += other._x
        self._y += other._y
