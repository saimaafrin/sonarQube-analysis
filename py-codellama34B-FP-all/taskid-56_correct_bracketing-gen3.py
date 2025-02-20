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

    stack = []

    for ch in brackets:
        if ch == '<':
            stack.append(ch)
        elif ch == '>':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False
