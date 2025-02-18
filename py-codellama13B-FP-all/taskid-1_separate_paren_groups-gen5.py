from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """


    if not paren_string:
        return []
    
    stack = []
    result = []
    current = ''

    for char in paren_string:
        if char == '(':
            if not stack:
                current += char
            stack.append(char)
        elif char == ')':
            stack.pop()
            if not stack:
                current += char
                result.append(current)
                current = ''
    return result
