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

    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            if len(stack) >= 2 and stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
            else:
                stack.pop()
    return not stack
