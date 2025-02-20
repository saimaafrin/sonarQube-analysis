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


    # Write your code here.
    # open_brackets and close_brackets are lists containing the respective open and closing bracket symbols.
    open_brackets = ["(", "{", "["]
    close_brackets = [")", "}", "]"]
    stack = []

    # Iterate through the given bracketing string.
    for bracket in brackets:
        # If the bracket is an opening bracket, append it to the stack.
        if bracket in open_brackets:
            stack.append(bracket)
        # If the bracket is a closing bracket, pop the top element of the stack.
        # If the closing bracket corresponds to the top element of the stack, move on to the next iteration.
        # If the closing bracket does not correspond to the top element of the stack, return False.
        else:
            if len(stack) > 0 and stack[-1] == close_brackets[open_brackets.index(bracket)]:
                stack.pop()
            else:
                return False
    # If the stack is empty at the end of the iteration, return True.
    if len(stack) == 0:
        return True
    # If the stack is not empty at the end of the iteration, return False.
    else:
        return False
