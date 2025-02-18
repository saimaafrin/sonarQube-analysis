from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_paren = '('
    close_paren = ')'

    string_list = paren_string.split()
    paren_string = ''
    for string in string_list:
        paren_string += string

    paren_groups = []
    current_group = ''
    for paren in paren_string:
        if paren == open_paren:
            current_group += paren
        if paren == close_paren:
            current_group += paren
            if is_valid_group(current_group):
                paren_groups.append(current_group)
                current_group = ''

    return paren_groups
