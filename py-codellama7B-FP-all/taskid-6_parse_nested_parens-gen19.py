from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_level = 0
    deepest_levels = []
    for char in paren_string:
        if char == '(':
            nested_level += 1
        elif char == ')':
            nested_level -= 1
        if nested_level > 0:
            if nested_level not in deepest_levels:
                deepest_levels.append(nested_level)
    return deepest_levels
