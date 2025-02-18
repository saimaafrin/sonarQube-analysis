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

    bracket_stack = []
    for bracket in brackets:
        if bracket == '>':
            if bracket_stack == []:
                return False
            else:
                bracket_stack.pop()
        else:
            bracket_stack.append(bracket)
    return not bracket_stack
