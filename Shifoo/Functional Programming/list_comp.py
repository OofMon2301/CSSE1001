def square_odds(xs: list[int]) -> list[int]:
    """
    >>> square_odds([1, 2, 3])
    [1, 9]
    """
    # Need to use list comprehension
    return [x ** 2 for x in xs if x % 2 == 1]