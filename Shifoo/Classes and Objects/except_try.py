def try_int(cs: str) -> int:
    """try_int
    converts a string to an integer. Unlike the built-in function int your try_int should return None if the conversion fails (not raise an exception. Use a try/except statement to achieve this
    >>> try_int("123")
    123
    >>> try_int("Hello World")  # Returns none

    >>> 
    """
    try:
        return int(cs)
    except ValueError:
        return None