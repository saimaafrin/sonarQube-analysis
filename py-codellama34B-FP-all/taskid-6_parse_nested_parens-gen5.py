from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_level = 0
    current_level = 0
    result = []
    for p in paren_string:
        if p == '(':
            current_level += 1
            max_level = max(max_level, current_level)
        elif p == ')':
            current_level -= 1
        else:
            raise ValueError(f'Invalid character {p} in {paren_string}')
    return result
