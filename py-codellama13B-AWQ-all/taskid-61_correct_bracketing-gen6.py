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

    # init
    stack = []
    for bracket in brackets:
        # (
        if bracket == '(':
            stack.append(bracket)
        # )
        else:
            # stack is empty
            if not stack:
                return False
            # stack is not empty
            else:
                stack.pop()
    # stack is empty
    if not stack:
        return True
    # stack is not empty
    else:
        return False
