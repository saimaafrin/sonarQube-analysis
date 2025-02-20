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

    if string == '':
        return False
    if string[0] == ']':
        return False
    if len(string) == 1:
        return True

    for i in range(len(string)):
        if string[i] == '[':
            if i == len(string) - 1:
                return False
            if string[i+1] == ']':
                return False
            return is_nested(string[i+1:])
        if string[i] == ']':
            if i == 0:
                return False
            if string[i-1] == '[':
                return is_nested(string[i+1:])
            return False
    return False
