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

    opening_brackets = []
    for b in brackets:
        if b == '(':
            opening_brackets.append(b)
        elif b == ')':
            if len(opening_brackets) == 0:
                return False
            else:
                opening_brackets.pop()

    if len(opening_brackets) > 0:
        return False

    return True
