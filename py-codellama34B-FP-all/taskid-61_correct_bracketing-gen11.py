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

    # this is a very common problem, you can look up the answer to see how
    # they did it, or look at the solution
    stack = []
    for ch in brackets:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
