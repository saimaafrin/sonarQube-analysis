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


    # start with one empty list, append strings to that list if they are '[' or ']'
    brackets = []
    for char in string:
        if char == '[':
            brackets.append(char)
        elif char == ']':
            if len(brackets) > 0 and brackets[-1] == '[':
                brackets.pop()
            else:
                brackets.append(char)

    return len(brackets) == 0
