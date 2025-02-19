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

    count = 0
    for s in brackets:
        if s == '(':
            count += 1
        elif s == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
