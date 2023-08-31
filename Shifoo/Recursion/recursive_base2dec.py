def base2dec(digits: list[int], base: int) -> int:
    """
    >>> base2dec([2, 3, 2, 2], 8)
    1234

    >>> base2dec([1, 2, 3], 5)
    38

    Preconditions:
    - digits is not empty
    0 < base <= 10
    for all d in digits: 0 <= d < base
    """
    if len(digits) == 1:
        return digits[0]
    else:
        return base2dec(digits[:-1], base) * base + digits[-1]
