from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    group_list = []
    paren_string = paren_string.replace(" ", "")
    start = 0
    while start < len(paren_string):
        stack = []
        for i, char in enumerate(paren_string[start:]):
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()
            if not stack:
                group_list.append(paren_string[start:start+i+1])
                start += i+1
                break
    return group_list
