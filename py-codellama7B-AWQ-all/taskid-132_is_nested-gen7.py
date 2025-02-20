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

    open_brackets = []
    for char in string:
        if char == '[':
            open_brackets.append(char)
        elif char == ']':
            if len(open_brackets) > 0:
                open_brackets.pop()
            else:
                return False
    if len(open_brackets) > 0:
        return True
    else:
        return False
