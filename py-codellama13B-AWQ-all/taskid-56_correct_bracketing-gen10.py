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

    stack = list()
    for b in brackets:
        if b == '<':
            stack.append(b)
        elif b == '>':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0
