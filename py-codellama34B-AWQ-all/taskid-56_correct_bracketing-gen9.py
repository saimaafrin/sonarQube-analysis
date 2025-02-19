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

    opening_brackets = []

    for bracket in brackets:
        if bracket == '<':
            opening_brackets.append(bracket)
        else:
            if len(opening_brackets) == 0:
                return False
            else:
                opening_brackets.pop()

    if len(opening_brackets) > 0:
        return False

    return True
