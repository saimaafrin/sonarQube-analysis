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
    current_group = []
    in_current_group = False
    for char in paren_string:
        if char == "(":
            if not in_current_group:
                in_current_group = True
            current_group.append(char)
        elif char == ")":
            current_group.append(char)
            result.append("".join(current_group))
            current_group = []
            in_current_group = False
        else:
            if in_current_group:
                current_group.append(char)
    return result
