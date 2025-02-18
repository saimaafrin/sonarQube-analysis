def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing('(')
    False
    >>> correct_bracketing('()')
    True
    >>> correct_bracketing('(()())')
    True
    >>> correct_bracketing(')(()')
    False
    """


    if len(brackets) == 0:
        return False
    if len(brackets) == 1:
        return False
    if len(brackets) == 2:
        return True

    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
