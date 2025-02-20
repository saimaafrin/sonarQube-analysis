def is_nested(string: str) -> bool:
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    >>> is_nested('[]')
    False
    >>> is_nested('[[][]]')
    True
    >>> is_nested('[[]][[')
    True
    """

    # Check that the string is non-empty
    if len(string) == 0:
        return False

    # Create a stack to keep track of the opening and closing brackets
    stack = []

    # Iterate over each character in the string
    for char in string:
        # If the current character is an opening bracket, push it onto the stack
        if char == '[':
            stack.append(char)
        # If the current character is a closing bracket
        elif char == ']':
            # If there are no more opening brackets on the stack, return False
            if len(stack) == 0:
                return False
            # Otherwise, pop the last opening bracket off the stack and continue
            else:
                stack.pop()

    # If there are still opening brackets on the stack at the end, return False
    return len(stack) == 0
