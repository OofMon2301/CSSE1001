def recursive_index(xs: list, index_path: list[int]):
    """
    >>> xs = [[[1, 2], 3], [4, 5, [6, 7]], 8, [9, 10, 11]]
    >>> recursive_index(xs, [1])
    [4, 5, [6, 7]]
    >>> recursive_index(xs, [1, 2])
    [6, 7]
    >>> recursive_index(xs, [1, 2, 0])
    6
    """
    # Check if index_path is empty
    if not index_path:
        return xs
    if len(index_path) == 1:
        return xs[index_path[0]]
    else:
        return recursive_index(xs[index_path[0]], index_path[1:])
