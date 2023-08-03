def find_functions(filename):
    with open(filename, "r") as f:
        # Read the file
        line = f.readlines()
        # Print out each line
        print(line)
        # If the line starts with def, write to txt file
        if line == "def":
            with open("functions.txt", "w") as f:
                f.write(line)
        # Close the file
        f.close()


print("What file do you want to write to?")
filename = input()
