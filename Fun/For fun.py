# Create a class


class HowDoesThisWork(object):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_x(self) -> int:
        """get_x Return a sum of all the x together

        _extended_summary_

        Returns:
            int: _description_
        """
        sum = 0
        for i in self.x:
            sum += i
        return sum

    def get_y(self) -> float:
        """get_y Gets the mean value of the y

        _extended_summary_

        Returns:
            int: _description_
        """
        mean_value = sum(self.y) / len(self.y)
        return mean_value

    def __str__(self) -> str:
        """__str__ Returns a string representation of the object

        _extended_summary_

        Returns:
            str: _description_
        """
        return f"({self.x}, {self.y})"

    def get_x_and_y(self) -> int:
        """get_x_and_y Returns the x and y values multiplied and to the power of a constant

        _extended_summary_

        Returns:
            int: _description_
        """
        power = int(input("Enter a power: "))
        return object.get_x() ** power * object.get_y() ** power


# Start defining the variables asking user for input

x = [int(i) for i in input("Enter a list of numbers for x: ").split()]
y = [int(i) for i in input("Enter a list of numbers for y: ").split()]


# Create an object
object = HowDoesThisWork(x, y)

# Show each variable individually
print(f"The sum of x is {object.get_x()}")
print(f"The mean value of y is {object.get_y()}")
print(f"The string representation of the object is {object.__str__()}")
print(
    f"The x and y values multiplied and to the power of a constant is {object.get_x_and_y()}"
)
