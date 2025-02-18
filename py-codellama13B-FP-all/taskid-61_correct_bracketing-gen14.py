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

    # start with 0
    result = 0
    for char in brackets:
        if char == "(":
            result += 1
        elif char == ")":
            result -= 1
        if result < 0:
            # if result < 0, means unmatched closing bracket.
            return False
    return result == 0
