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
    current_group = ''
    stack = []

    for char in paren_string:
        if char in ['(', '{', '[']:
            stack.append(char)
            current_group += char
        if char in [')', '}', ']']:
            if len(stack) == 0 or stack.pop() != '(' if char == ')' else '[' if char == ']' else '{':
                return []
            current_group += char
            if len(stack) == 0:
                result.append(current_group)
                current_group = ''

    return result
