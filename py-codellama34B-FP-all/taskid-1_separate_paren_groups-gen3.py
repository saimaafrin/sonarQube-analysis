from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # your code here
    stack = []
    groups = []
    start = None

    for i, p in enumerate(paren_string):
        if p == '(':
            if not stack:
                start = i
            stack.append(p)
        elif p == ')':
            stack.pop()
            if not stack:
                groups.append(paren_string[start: i + 1])
    return groups
