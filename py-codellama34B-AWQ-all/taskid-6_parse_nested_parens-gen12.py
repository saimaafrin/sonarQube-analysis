from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_groups = paren_string.split()
    max_levels = []
    for paren_group in paren_groups:
        level = 0
        for char in paren_group:
            if char == '(':
                level += 1
            if char == ')':
                level -= 1
        max_levels.append(level)
    return max_levels
