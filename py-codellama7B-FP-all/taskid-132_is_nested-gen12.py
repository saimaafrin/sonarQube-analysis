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

    for c in string:
        if c == "[" and not stack:
            stack.append(c)
        elif c == "[" and stack:
            stack.append(c)
        elif c == "]" and stack:
            stack.pop()
        elif c == "]" and not stack:
            return False

    return False if stack else True
