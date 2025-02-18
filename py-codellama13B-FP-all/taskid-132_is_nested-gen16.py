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
    for bracket in string:
        if bracket == '[':
            open_brackets.append(bracket)
        elif bracket == ']':
            if len(open_brackets) == 0:
                return False
            open_brackets.pop()
    return len(open_brackets) > 0
