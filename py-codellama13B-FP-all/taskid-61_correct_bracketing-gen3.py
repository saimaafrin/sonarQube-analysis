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

    open_brackets = []
    for char in brackets:
        if char == '(':
            open_brackets.append(char)
        elif char == ')':
            if len(open_brackets) == 0:
                return False
            open_brackets.pop()
    return len(open_brackets) == 0
