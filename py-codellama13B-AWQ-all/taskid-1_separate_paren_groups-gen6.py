from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.replace(' ', '')
    start_pos = 0
    res = []
    while start_pos < len(paren_string):
        end_pos = paren_string.find('(', start_pos)
        if end_pos == -1:
            end_pos = len(paren_string)
        res.append(paren_string[start_pos:end_pos])
        start_pos = end_pos
    return res
