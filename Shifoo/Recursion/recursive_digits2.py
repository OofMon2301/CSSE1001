def dec2base(n: int, b: int) -> list[int]:
    """
    >>> dec2base(1234, 10)
    [1, 2, 3, 4]

    >>> dec2base(1234, 8)
    [2, 3, 2, 2]
    """
    if n < b:
        return [n]
    else:
        return dec2base(n // b, b) + [n % b]
