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
    current_group = ''
    current_level = 0

    for character in paren_string:
        if character != ' ':
            current_group += character
            if character == '(':
                current_level += 1
            elif character == ')':
                current_level -= 1
                if current_level == 0:
                    groups.append(current_group)
                    current_group = ''
    return groups
