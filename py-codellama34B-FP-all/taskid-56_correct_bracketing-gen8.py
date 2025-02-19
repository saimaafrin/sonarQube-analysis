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

    # use a stack to keep track of unmatched '<'
    stack = []
    for char in brackets:
        if char == '<':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # if stack is empty after iterating through all brackets, brackets are properly bracketed
    return len(stack) == 0
