def all_gt(xs: list[int], n: int) -> list[int]:
    """all_gt Return the list of all numbers from nums that are bigger than n."""
    x = []
    for i in xs:
        if i > n:
            x.append(i)
    return x
