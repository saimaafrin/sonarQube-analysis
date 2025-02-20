def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing('<')
    False
    >>> correct_bracketing('<>')
    True
    >>> correct_bracketing('<<><>>')
    True
    >>> correct_bracketing('><<>')
    False
    """

    brackets_stack = []
    for bracket in brackets:
        if bracket == "<":
            brackets_stack.append(bracket)
        else:
            if len(brackets_stack) == 0:
                return False
            brackets_stack.pop()
    return len(brackets_stack) == 0
