from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parenthesis = ['(']
    close_parenthesis = [')']
    open_counter = 0
    close_counter = 0
    groups = []
    current_group = ''

    for char in paren_string:
        if char in open_parenthesis:
            open_counter += 1
            current_group += char
        elif char in close_parenthesis:
            close_counter += 1
            current_group += char

        if open_counter == close_counter and current_group != '':
            groups.append(current_group)
            current_group = ''
            open_counter = 0
            close_counter = 0

    return groups
