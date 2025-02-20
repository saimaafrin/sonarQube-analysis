from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    group = ''
    groups = []
    for paren in paren_string:
        if paren == ')':
            if group.count('(') > group.count(')'):
                group += paren
            else:
                groups.append(group)
                group = ''
        elif paren == '(':
            group += paren
        else:
            group += paren
    groups.append(group)
    return groups
