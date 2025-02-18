from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    groups = []
    group = ''
    for char in paren_string:
        if char in '()':
            group += char
        elif char.isspace():
            continue
        elif char == ')':
            if group.endswith(')'):
                groups.append(group)
                group = ''
            else:
                raise ValueError("Unbalanced parentheses")
    if group:
        raise ValueError("Unbalanced parentheses")
    return groups
