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

    # 1. create a stack
    stack = []

    # 2. iterate over the string
    for i in range(len(string)):

        # 3. if we hit an opening bracket, put it on the stack
        if string[i] == '[':
            stack.append(string[i])

        # 4. if we hit a closing bracket, see if there's an opening bracket in the stack. If there is, remove it. Otherwise, return False
        elif string[i] == ']':

            if len(stack) == 0:
                return False

            if stack[-1] != '[':
                return False

            stack.pop()

    # 5. if the stack is not empty at the end of the iteration, return False
    if len(stack) != 0:
        return False

    # 6. if we made it to the end of the iteration and the stack is empty, return True
    return True
