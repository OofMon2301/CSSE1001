def mean(xs: list[int]) -> float:
    """ """
    # >>> mean([2, 7, 3, 9, 13])
    # 6.8
    total = 0
    for i in xs:
        total += i
    return total / len(xs)
