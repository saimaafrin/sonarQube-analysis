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

    opening_brackets = set()
    for bracket in brackets:
        if bracket == '<':
            opening_brackets.add(bracket)
        elif bracket == '>':
            if len(opening_brackets) == 0:
                return False
            opening_brackets.remove(bracket)
    return len(opening_brackets) == 0
