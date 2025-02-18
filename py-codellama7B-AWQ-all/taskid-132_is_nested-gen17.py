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

    brackets = ['[',']']
    stack = []
    for ch in string:
        if ch in brackets:
            if ch == brackets[0]:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
    return len(stack) == 0
