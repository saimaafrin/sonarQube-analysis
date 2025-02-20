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
    counter = 0
    temp_group = ''
    for char in paren_string:
        if char == '(':
            counter += 1
            temp_group += char
        elif char == ')':
            counter -= 1
            temp_group += char
        if counter == 0:
            groups.append(temp_group)
            temp_group = ''
    return groups
