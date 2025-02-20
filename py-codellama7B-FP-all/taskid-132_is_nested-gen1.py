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

    open_list, close_list = [], []
    for char in string:
        if char == '[':
            open_list.append(char)
        elif char == ']':
            close_list.append(char)

    if not open_list and not close_list:
        return False

    for i in range(len(open_list) - 1, -1, -1):
        if open_list[i] in close_list:
            close_list.remove(open_list[i])
            open_list.pop(i)

    return not close_list
