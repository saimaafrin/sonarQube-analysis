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

    if len(brackets) % 2 == 1:
        return False
    if len(brackets) == 0:
        return True
    stack = [brackets[0]]
    for i in range(1, len(brackets)):
        if brackets[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append(brackets[i])
    if len(stack) > 0:
        return False
    else:
        return True
