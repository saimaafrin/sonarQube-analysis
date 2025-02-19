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

    # Your code goes here
    left_counter = 0
    right_counter = 0
    for i in string:
        if i == '[':
            left_counter += 1
        else:
            right_counter += 1

        if left_counter == right_counter:
            return True

    return left_counter > right_counter
