from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result: List[int] = []

    paren_string = paren_string.strip()
    group_count = paren_string.count(' ')

    if group_count == 0:
        result.append(get_max_parens(paren_string))

    if group_count > 0:
        groups = paren_string.split()
        for group in groups:
            result.append(get_max_parens(group))

    return result
