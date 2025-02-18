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

    opening = set()
    for c in brackets:
        if c == '(':
            opening.add(c)
        elif c == ')':
            if len(opening) == 0:
                return False
            opening.remove(c)
    return len(opening) == 0
