from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.strip()
    paren_string = paren_string.replace(" ", "")
    groups = []
    current_group = ""
    for i, char in enumerate(paren_string):
        if char in "(":
            current_group += char
            paren_string = paren_string[i+1:]
            break
    for char in paren_string:
        if char == "(":
            current_group += char
        elif char == ")":
            current_group += char
        if char == ")":
            if current_group.count("(") == current_group.count(")"):
                groups.append(current_group)
                current_group = ""
    return groups
