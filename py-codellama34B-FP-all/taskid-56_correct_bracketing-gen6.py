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

    opening = 0
    for bracket in brackets:
        if bracket == '<':
            opening += 1
        else:
            opening -= 1
            if opening < 0:
                return False
    return opening == 0
