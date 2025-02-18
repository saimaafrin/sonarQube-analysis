from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # 1. Write a recursive function which takes a string as input and returns a list of strings
    #    - If the string is empty, return an empty list
    #    - If the string contains only a single group, return a list with that group
    #    - If the string contains multiple groups, split the string into two strings at the last closing brace
    #      and append the returned list from each string to the current list and return that
    # 2. If the string is not empty, but does not have a closing brace, return an empty list
    # 3. If the string is not empty and has a closing brace, recursively call the function on each of the two
    #    resulting strings and append the returned list from each string to the current list and return that
    return []
