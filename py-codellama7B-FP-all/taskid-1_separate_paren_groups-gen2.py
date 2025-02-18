from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    string_split_at_brackets = paren_string.split('()')
    string_list = []
    for string in string_split_at_brackets:
        if string.find('(') != -1 and string.find(')') != -1:
            string_list.append(string)
    return string_list
