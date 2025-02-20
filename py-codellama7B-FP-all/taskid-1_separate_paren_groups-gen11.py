from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    balanced_strings = []
    current_string = ''
    for char in paren_string:
        if char == '(':
            current_string += char
        elif char == ')':
            current_string += char
            if current_string.count('(') == current_string.count(')'):
                balanced_strings.append(current_string)
                current_string = ''
        else:
            current_string += char
    return balanced_strings
