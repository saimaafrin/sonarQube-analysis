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

    # Initialize a stack
    stack = []
    # Iterate over the string
    for char in brackets:
        # If char is an opening bracket
        if char == '<':
            # Add the char to the stack
            stack.append(char)
        # Else If char is a closing bracket
        elif char == '>':
            # If the stack is empty
            if not stack:
                # Return False
                return False
            # Else
            else:
                # Pop the top item of the stack
                stack.pop()
    # If the stack is not empty
    if stack:
        # Return False
        return False
    # Else
    else:
        # Return True
        return True
