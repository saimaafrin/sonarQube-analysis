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

    left_bracket_count = 0
    right_bracket_count = 0
    for c in string:
        if c == '[':
            left_bracket_count += 1
        else:
            right_bracket_count += 1
            if right_bracket_count > left_bracket_count:
                return False
    return left_bracket_count == right_bracket_count
