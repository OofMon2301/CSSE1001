def get_number(string):
    """Returns the number from string."""
    number = ""
    for char in string:
        if char.isdigit():
            number += char
    return int(number)
