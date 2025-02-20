from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """


    paren_group_list = []

    current_group = ''
    brace_count = 0
    for char in paren_string:
        if char == '(':
            brace_count += 1
            current_group += char
        elif char == ')':
            brace_count -= 1
            current_group += char
        else:
            continue

        if brace_count == 0:
            paren_group_list.append(current_group)
            current_group = ''

    return paren_group_list
