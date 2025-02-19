from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parenthesis = 0
    start = 0
    result = []

    for i, char in enumerate(paren_string):
        if char == '(':
            if open_parenthesis == 0:
                start = i
            open_parenthesis += 1
        elif char == ')':
            open_parenthesis -= 1
            if open_parenthesis == 0:
                result.append(paren_string[start:i + 1])

    return result
