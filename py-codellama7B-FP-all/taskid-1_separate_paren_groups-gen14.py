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

    current_group = []
    for c in paren_string:
        if c == '(':
            current_group.append(c)
        elif c == ')':
            current_group.append(c)
            if len(current_group) == 1:
                result.append(''.join(current_group))
                current_group = []
            else:
                current_group.pop()
        else:
            current_group.append(c)

    if current_group:
        result.append(''.join(current_group))

    return result
