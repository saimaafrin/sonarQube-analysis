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
    open_paren_groups = []
    list_groups = []
    counter = 0
    for i in paren_string:
        if i == '(':
            open_paren_groups.append(counter)
            counter += 1
        if i == ')':
            counter -= 1
            if counter == 0:
                list_groups.append(paren_string[open_paren_groups.pop():counter+1])
                counter = 0
    return list_groups
