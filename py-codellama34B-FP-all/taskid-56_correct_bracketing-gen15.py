def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing('<')
    False
    >>> correct_bracketing('<>')
    True
    >>> correct_bracketing('<<><>>')
    True
    >>> correct_bracketing('><<>')
    False
    """

    if brackets == "":
        return True
    elif brackets[0] == "<":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == ">":
        return False
    else:
        raise ValueError("Invalid bracketing string")
