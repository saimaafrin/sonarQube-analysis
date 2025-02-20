from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # The basic idea is to iterate through the string and keep track of the paren level. Whenever we hit a new level,
    # we start a new string in the output.
    output: List[str] = []
    current_string = ''
    current_level = 0

    for char in paren_string:
        if char == '(':
            current_level += 1
            current_string += char
        elif char == ')':
            current_level -= 1
            current_string += char

            # Whenever we go to a lower level, we should output the current string and start a new one.
            if current_level == 0:
                output.append(current_string)
                current_string = ''
        else:
            current_string += char

    if current_string:
        output.append(current_string)

    return output
