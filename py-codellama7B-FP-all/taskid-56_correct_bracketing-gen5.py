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

    open_brackets = ['<']
    for bracket in brackets:
        if bracket == '<':
            open_brackets.append(bracket)
        elif bracket == '>':
            if len(open_brackets) == 0:
                return False
            open_brackets.pop()
    if len(open_brackets) != 0:
        return False
    return True
