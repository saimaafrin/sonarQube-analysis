from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_levels = []
    for paren_str in paren_string.split():
        level = 0
        for paren in paren_str:
            if paren == '(':
                level += 1
            else:
                level -= 1
        nested_levels.append(level)
    return nested_levels
