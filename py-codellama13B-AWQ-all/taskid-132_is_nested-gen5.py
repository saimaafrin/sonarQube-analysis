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

    # init
    stack = []
    length = len(string)
    open_brace = 0
    close_brace = 0

    # validate string
    if length <= 0:
        return False

    # count braces
    for i in range(length):
        if string[i] == '[':
            open_brace += 1
        elif string[i] == ']':
            close_brace += 1

    # if brackets are not balanced
    if open_brace != close_brace:
        return False

    # check nesting
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) > 0
