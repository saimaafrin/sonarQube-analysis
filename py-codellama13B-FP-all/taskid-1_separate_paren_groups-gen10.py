from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    output = []
    current_group = ''
    # If there is more than one group, we can assume that the last closing parenthesis is for the first group
    while len(paren_string) > 0:
        current_group = ''
        while True:
            if paren_string[0] == ')':
                raise ValueError('Closing parenthesis found before opening parenthesis')
            if paren_string[0] == '(':
                current_group += '('
                paren_string = paren_string[1:]
                break
            else:
                current_group += paren_string[0]
                paren_string = paren_string[1:]
        if current_group[0] == '(':
            # If we have an opening parenthesis, we know that the last closing parenthesis is for the previous group
            output.append(current_group)
            break
        else:
            current_group = ''
    return output
