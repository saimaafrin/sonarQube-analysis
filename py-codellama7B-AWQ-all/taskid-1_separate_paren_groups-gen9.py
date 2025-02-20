from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    groups: List[str] = []
    current: List[str] = []
    open_paren_count = 0
    for c in paren_string:
        if c == "(":
            open_paren_count += 1
            current.append(c)
        elif c == ")":
            open_paren_count -= 1
            if open_paren_count > 0:
                current.append(c)
            else:
                groups.append("".join(current))
                current = []
        else:
            current.append(c)
    if current != []:
        groups.append("".join(current))
    return groups
