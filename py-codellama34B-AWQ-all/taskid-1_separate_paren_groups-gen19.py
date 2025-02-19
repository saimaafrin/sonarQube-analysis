from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []
    stack = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            stack.append(i)
        elif paren_string[i] == ')':
            if len(stack) == 1:
                result.append(paren_string[stack[0]:i+1])
                stack.pop()
            else:
                stack.pop()
    return result
