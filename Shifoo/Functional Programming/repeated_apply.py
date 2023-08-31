def compose(f: callable, g: callable) -> callable:
    """
    Return the composition of f and g.

    """
    return lambda x: f(g(x))


def repeatedly_apply(f: callable, n: int) -> callable:
    """
    that takes a function f of one argument and a positive integer n and returns the n-fold composition of f.
    """
    # Has to be recursive
    if n == 1:
        return f
    else:
        return compose(f, repeatedly_apply(f, n - 1))
