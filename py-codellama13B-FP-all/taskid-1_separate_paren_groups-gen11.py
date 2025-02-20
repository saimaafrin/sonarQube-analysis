from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []
    current_paren_group = []
    paren_level = 0
    for c in paren_string:
        if c == '(':
            if paren_level == 0:
                current_paren_group = []
            paren_level += 1
        else:
            if c == ')':
                paren_level -= 1
                if paren_level == 0:
                    result.append(''.join(current_paren_group))
            if paren_level > 0:
                current_paren_group.append(c)
    return result
