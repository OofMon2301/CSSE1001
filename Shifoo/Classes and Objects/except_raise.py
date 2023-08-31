class InvalidCommand(Exception):
    """
    Do not modify this.
    """

    pass


def validate_input(cs: str) -> tuple[str, list[float]]:
    """validate_input takes a string and returns the pair (command, [arg1,arg2]) if the string is valid and the args are valid floats.
    If the string is not valid, it raises InvalidCommand.



    Example:

        >>> validate_input('add 2.3 1.7')
        ['add', 2.3, 1.7]

        >>> validate_input('takeaway 2.3 1.7')
        InvalidCommand

        >>> validate_input('mul 2 pi')
        InvalidCommand
    """
    try:
        command, *args = cs.split()
        if command not in ["add", "sub", "mul", "div"]:
            raise InvalidCommand
        # Must have 2 args
        if len(args) != 2:
            raise InvalidCommand
        args = [float(arg) for arg in args]
        return command, args
    except ValueError:
        raise InvalidCommand
