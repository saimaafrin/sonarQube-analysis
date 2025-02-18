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

    open_bracket_stack = []
    for bracket in brackets:
        if bracket == '(':
            open_bracket_stack.append(bracket)
        elif bracket == ')':
            if len(open_bracket_stack) == 0:
                return False
            open_bracket_stack.pop()
    return len(open_bracket_stack) == 0
