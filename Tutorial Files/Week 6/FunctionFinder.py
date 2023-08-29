# Define a function named find_functions that takes a filename as an argument
def find_functions(filename):
    """find_functions Finds every function in the file and writes to another file

    Args:
        filename (_type_): The filename of the file to be read
    """
    # Open the file with the given filename in read mode
    with open(filename, "r") as f:
        # Read the first line of the file
        lines = f.readline()
        # Read until the end of the file
        while lines != "":
            # If the line starts with "def", it is a function definition
            if lines.startswith("def "):
                # Open a new file named "functions.txt" in append mode
                with open("functions.txt", "a") as f2:
                    # Write the line to the new file
                    f2.write(lines)
            # Read the next line of the file
            lines = f.readline()
        # Write the functions to a new file named "functions.txt"


# Call the find_functions function with the argument "C:/Users/jamie/OneDrive/2023/CSSE1001/Tutorial Files/Week 6/week06_functions.py"
find_functions(
    "C:/Users/jamie/OneDrive/2023/CSSE1001/Tutorial Files/Week 6/week06_functions.py"
)

name = input("Enter your name: ")
with open(name, "r") as f:
    lines = f.readline()
    while lines != "":
        print(lines)
        lines = f.readline()