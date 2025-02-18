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

    open_bracket = 0
    close_bracket = 0
    for i in range(len(string)):
        if string[i] == '[':
            open_bracket += 1
        elif string[i] == ']':
            close_bracket += 1
            if close_bracket > open_bracket:
                return False

    if open_bracket == close_bracket:
        return False
    else:
        return True
