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

    counter = 0
    for bracket in brackets:
        if bracket == '(':
            counter += 1
        elif bracket == ')':
            counter -= 1
        if counter < 0:
            return False
    return True if counter == 0 else False
