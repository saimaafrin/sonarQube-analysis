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
    assert len(paren_string) > 0
    paren_groups = []
    start_index = 0
    while start_index < len(paren_string):
        if paren_string[start_index] == '(':
            open_count = 1
            for i in range(start_index + 1, len(paren_string)):
                if paren_string[i] == '(':
                    open_count += 1
                elif paren_string[i] == ')':
                    open_count -= 1
                if open_count == 0:
                    paren_groups.append(paren_string[start_index:i + 1])
                    start_index = i + 1
                    break
    return paren_groups
