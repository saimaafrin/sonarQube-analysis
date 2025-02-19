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

    # stack to store all opening brackets
    bracket_stack = []
    # iterate over all chars
    for char in brackets:
        # if char is opening bracket, push to stack
        if char == '(':
            bracket_stack.append(char)
        # if char is closing bracket and stack is not empty
        elif char == ')' and bracket_stack:
            # pop the top of the stack, as closing bracket found
            bracket_stack.pop()
        # if char is closing bracket and stack is empty
        elif char == ')' and not bracket_stack:
            # return False, closing bracket without opening bracket
            return False
    # if all brackets matched and stack is empty, return True
    return not bracket_stack
