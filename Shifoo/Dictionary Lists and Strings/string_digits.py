def get_digits(cs: str) -> str:
    """removes all non-digits in the string."""
    for i in cs:
        if not i.isdigit():
            cs = cs.replace(i, "")
    return cs
