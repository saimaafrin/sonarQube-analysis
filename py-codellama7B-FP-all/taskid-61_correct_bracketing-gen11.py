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

    opening = '([{'
    closing = ')]}'
    stack = []
    for char in brackets:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            top = stack.pop()
            if opening.index(top) != closing.index(char):
                return False
    if stack:
        return False
    return True
