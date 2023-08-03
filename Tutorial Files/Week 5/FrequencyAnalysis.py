def letter_frequency(message):
    """Returns a dictionary of each letter and its frequency in the message."""
    # Create a dictionary to store the letter frequencies
    frequencies = {}
    # For each letter in the message
    for letter in message:
        # If the letter is not already in the dictionary
        if letter not in frequencies:
            # Add the letter to the dictionary with a value of 0
            frequencies[letter] = 0
        # Increment the value of the letter in the dictionary
        frequencies[letter] += 1
    # Return the dictionary
    return frequencies


def max_letters(message):
    """Returns the letter with the highest frequency."""
    highest = 0
    for letter in message:
        if message[letter] > highest:
            highest = message[letter]
    return highest


# Interface
message = input("Enter a message: ")
print(letter_frequency(message))
print(
    "The letter with the highest frequency is: "
    + str(max_letters(letter_frequency(message)))
)
