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
    if string.count('[') != string.count(']'):
        return False
    i = 0
    while i < len(string):
        if string[i] == '[':
            if string[i+1] == '[':
                return True
        else:
            if string[i-1] == ']':
                return True
        i += 1
    return False
