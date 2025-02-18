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


    left_brackets = string.count('[')
    right_brackets = string.count(']')

    if left_brackets != right_brackets:
        return False

    stack = []
    for i, bracket in enumerate(string):
        if bracket == '[':
            stack.append(i)
        if bracket == ']':
            if stack:
                stack.pop()
            else:
                return False

    return True if stack else False
