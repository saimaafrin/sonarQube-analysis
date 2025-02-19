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
    buffer = ''
    count = 0
    for char in paren_string:
        if char in '()':
            if not buffer:
                buffer += char
            else:
                buffer += char
                count += 1
                if count % 2 == 0:
                    result.append(buffer)
                    buffer = ''
        else:
            pass
    if buffer:
        result.append(buffer)
    return result
