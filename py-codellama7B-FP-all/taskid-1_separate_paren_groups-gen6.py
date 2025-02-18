from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Your code here

    string = paren_string.replace(' ', '')
    result = []
    current = ''
    for char in string:
        if char == '(':
            current += char
        elif char == ')':
            if current[-1] == '(':
                result.append(current[1:])
                current = ''
            else:
                current += char
        else:
            current += char
    if current != '':
        result.append(current)
    return result
