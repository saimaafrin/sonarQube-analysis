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

    open_brackets = 0
    for bracket in brackets:
        if bracket == "<":
            open_brackets += 1
        else:
            open_brackets -= 1
            if open_brackets < 0:
                return False
    return open_brackets == 0
