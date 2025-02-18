from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parens = 0
    start = 0
    end = 0
    group_start = 0
    groups = []
    for i, char in enumerate(paren_string):
        if char == '(':
            open_parens += 1
        if char == ')':
            open_parens -= 1
        if open_parens == 0 and char == ')':
            groups.append(paren_string[start:i+1])
            start = i+1
        if char == '(' and open_parens == 0:
            group_start = i
    return groups
