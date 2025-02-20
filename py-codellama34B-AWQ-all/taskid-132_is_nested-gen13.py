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


    # counter for keeping track of number of open braces
    count = 0

    # Iterate through string
    for i in string:
        # Check if it is an opening brace
        if i == '[':
            count += 1

        # Check if it is a closing brace
        elif i == ']':
            # If the closing brace is not the last brace, 
            # and there has been no opening brace before it,
            # return False
            if count == 0:
                return False
            # Decrement count for every closing brace
            count -= 1

    # if count is not 0 i.e. all braces are not closed, return False
    return count == 0
