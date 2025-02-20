from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_levels = []
    current_level = 0
    for i, s in enumerate(paren_string):
        if s == '(':
            current_level += 1
        elif s == ')':
            current_level -= 1
        if i > 0 and paren_string[i - 1] == '(' and current_level == 0:
            paren_levels.append(current_level)
            current_level = 0
    return paren_levels
