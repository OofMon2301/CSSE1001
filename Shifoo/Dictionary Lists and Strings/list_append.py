def add_sizes(strings: list[str]) -> list[tuple[str, int]]:
    """Return a list of pairs consisting of the elements of strings with their sizes."""
    x = []
    for i in strings:
        x.append((i, len(i)))

    return x


print(add_sizes(["a", "bc", "def"]))  # [('a', 1), ('bc', 2), ('def', 3)]
