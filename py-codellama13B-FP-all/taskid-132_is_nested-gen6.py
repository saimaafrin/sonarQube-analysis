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

    # Initialize the stack
    stack = []
    
    # Iterate over the string
    for char in string:
        # If the current character is a left bracket, push it onto the stack
        if char == '[':
            stack.append(char)
        # If the current character is a right bracket, and there are no left brackets on the stack, return False
        elif char == ']':
            if len(stack) == 0:
                return False
        # If the current character is a right bracket and there is a left bracket on the stack, pop the left bracket off and continue
        elif char == ']':
            stack.pop()
    
    # If there are any left brackets left in the stack, return False
    if len(stack) != 0:
        return False
    else:
        return True
