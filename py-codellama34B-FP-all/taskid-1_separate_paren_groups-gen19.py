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
    index = 0
    stack = []
    while index < len(paren_string):
        char = paren_string[index]
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        if len(stack) == 0:
            result.append(paren_string[index - len(result): index + 1])
        index += 1
    return result
