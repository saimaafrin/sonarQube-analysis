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
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            top = stack.pop()
            if top == '(':
                if len(stack) > 0:
                    top = stack.pop()
                    groups.append(top)
            else:
                stack.append(top)
                stack.append(char)
    if len(stack) > 0:
        groups.append(''.join(stack))
    return groups
