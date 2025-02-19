from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    stack = []
    i = 0
    result = []
    while i < len(paren_string):
        if paren_string[i] == '(':
            stack.append('(')
        elif paren_string[i] == ')':
            if len(stack) > 0:
                stack.pop()
            if len(stack) == 0:
                result.append(paren_string[i - len(stack):i + 1])
                stack.clear()
        i += 1
    return result
