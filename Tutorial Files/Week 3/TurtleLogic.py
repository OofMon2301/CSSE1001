import turtle

# Create a function for Rectangle


def interact():
    t = turtle.Turtle()
    turtle.speed(1)
    # Interact with the user
    print("Welcome to the Turtle Star Drawer")
    print("Enter the distance you want the turtle to move")
    print("Enter 'q' to quit")
    print("Enter 'r' to reset")

    distance = input("Enter the distance: ")
    while distance != "q":
        # Move turtle by interacting with the user
        direction = input("Direction: ")
        # Cardinal directions
        if direction == "n":
            t.setheading(90)
            t.forward(int(distance))
        if direction == "s":
            t.setheading(270)
            t.forward(int(distance))
        if direction == "e":
            t.setheading(0)
            t.forward(int(distance))
        if direction == "w":
            t.setheading(180)
            t.forward(int(distance))
        # If not cardinal directions, then print "Not a direction"
        if direction != ["n", "s", "e", "w"]:
            print("Not a direction")
            pass
        if distance == "r":
            t.reset()
        else:
            pass
    # Change the direction of the turtle through user input


def polygon():
    # Makes a polygon using turtle
    t = turtle.Turtle()
    turtle.speed(1)


def star():
    # Makes a star using the turtle
    t = turtle.Turtle()
    turtle.speed(100)
    while True:
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.right(144)
        t.forward(100)

# Execute main
if __name__ == "__main__":
    star()
