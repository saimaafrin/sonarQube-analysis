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

    assert isinstance(brackets, str) and all(c in "() " for c in brackets), "bad input"
    s = 0
    for c in brackets:
        if c == "(":
            s += 1
        elif c == ")":
            s -= 1
            if s < 0:
                return False
    return s == 0
