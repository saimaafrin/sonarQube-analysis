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


    open_count = 0
    close_count = 0
    for char in string:
        if char == "[":
            open_count += 1
        elif char == "]":
            close_count += 1

        if close_count > open_count:
            return False

    if open_count == close_count:
        return True
    else:
        return False
