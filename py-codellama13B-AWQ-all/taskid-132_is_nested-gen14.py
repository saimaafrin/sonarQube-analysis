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

    if not string:
        return False
    elif string[0] == ']':
        return False
    elif string[-1] == '[':
        return False
    elif string[0] == '[' and string[-1] == ']':
        return True
    else:
        return is_nested(string[1:-1])
