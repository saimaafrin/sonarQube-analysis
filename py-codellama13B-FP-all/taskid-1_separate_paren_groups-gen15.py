from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    stack = []
    output = []
    current_group = ""
    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            if stack[-1] == '(':
                stack.pop()
                current_group += char
            else:
                # We are in an error state. Stop processing the current group and move on.
                # (The current group will not be added to the output.)
                break
        if len(stack) == 0:
            # We have a complete group
            output.append(current_group)
            current_group = ""
    return output
