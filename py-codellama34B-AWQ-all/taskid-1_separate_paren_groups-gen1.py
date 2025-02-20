from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # check that each group of parentheses is properly balanced
    # (open-close, open-close, etc.)
    if paren_string.count('(') != paren_string.count(')'):
        raise ValueError('The number of left and right parentheses must be equal')
    paren_list = []
    groups = paren_string.split()
    for group in groups:
        if not is_balanced(group):
            raise ValueError(f'The group {group} is not properly balanced')
    current_group = ''
    for char in paren_string:
        if char == '(':
            if not current_group:
                current_group += char
            else:
                current_group += ' ' + char
        elif char == ')':
            current_group += char
            if current_group.count('(') == current_group.count(')'):
                paren_list.append(current_group)
                current_group = ''
    if current_group:
        paren_list.append(current_group)
    return paren_list
