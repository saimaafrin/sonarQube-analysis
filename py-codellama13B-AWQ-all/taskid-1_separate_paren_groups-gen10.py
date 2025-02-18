from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """


    result: List[str] = []

    def is_open_paren(c: str) -> bool:
        return c == "("

    def is_close_paren(c: str) -> bool:
        return c == ")"

    def is_close_paren_matching_previous(c: str, top: str) -> bool:
        return is_close_paren(c) and top == "("

    stack = []
    current_group: List[str] = []
    for char in paren_string:
        if char.isspace():
            continue
        if is_open_paren(char):
            stack.append(char)
            current_group.append(char)
        elif is_close_paren_matching_previous(char, stack[-1]):
            stack.pop()
            current_group.append(char)
        else:
            raise ValueError("Invalid string")
        if len(stack) == 0:
            result.append("".join(current_group))
            current_group = []

    if current_group:
        raise ValueError("Invalid string")

    return result
