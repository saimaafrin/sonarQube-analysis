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

    # bracketing is a stack to store the opening brackets
    bracketing = []

    for bracket in brackets:
        if bracket == '(':
            # push opening bracket to the stack
            bracketing.append(bracket)
        else:
            # pop an opening bracket from the stack
            if len(bracketing) == 0:
                return False
            bracketing.pop()

    # if all opening brackets have a closing bracket
    return len(bracketing) == 0
