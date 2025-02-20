from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    current_paren_level = 0
    nested_levels = []
    for character in paren_string:
        if character == '(':
            current_paren_level += 1
        elif character == ')':
            current_paren_level -= 1
        if current_paren_level > max(nested_levels):
            nested_levels.append(current_paren_level)
    return nested_levels
