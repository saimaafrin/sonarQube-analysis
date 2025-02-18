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


    count_open_brackets = 0

    for char in brackets:
        if char == "<":
            count_open_brackets += 1
        elif char == ">":
            count_open_brackets -= 1
            if count_open_brackets < 0:
                return False

    return count_open_brackets == 0
