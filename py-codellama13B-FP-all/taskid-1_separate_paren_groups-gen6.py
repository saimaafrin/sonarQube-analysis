from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.replace(" ", "")
    paren_groups = []
    start_ind = 0
    curr_depth = 0
    for i in range(len(paren_string)):
        char = paren_string[i]
        if char == '(':
            curr_depth += 1
        if char == ')':
            curr_depth -= 1
        if curr_depth == 0:
            paren_groups.append(paren_string[start_ind:i+1])
            start_ind = i+1
    return paren_groups
