from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    group_strings = []
    current_group = ''
    open_parens = 0
    for char in paren_string:
        if char == '(':
            open_parens += 1
            current_group += char
        elif char == ')':
            open_parens -= 1
            current_group += char
        else:
            current_group += char

        if open_parens == 0:
            group_strings.append(current_group)
            current_group = ''
    return group_strings
