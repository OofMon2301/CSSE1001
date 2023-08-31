def get_digits(n: int) -> list[int]:
    """
    >>> get_digits(123)
    [1, 2, 3]
    """
    if n < 10:
        return [n]
    else:
        return get_digits(n // 10) + [n % 10]
