from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """


    if paren_string == '':
        return []

    result = []
    current_group = ''
    i = 0
    count_left = 0
    count_right = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            count_left += 1
            current_group += '('
        elif paren_string[i] == ')':
            count_right += 1
            current_group += ')'
            if count_left == count_right:
                result.append(current_group)
                current_group = ''
                count_left = 0
                count_right = 0
        else:
            current_group += paren_string[i]
        i += 1

    return result
