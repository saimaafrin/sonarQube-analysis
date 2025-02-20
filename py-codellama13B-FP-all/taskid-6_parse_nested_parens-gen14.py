from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_nesting_level = []
    for i in paren_string.split():
        current_nesting_level = 0
        for j in i:
            if j == '(':
                current_nesting_level += 1
            if j == ')':
                current_nesting_level -= 1
        max_nesting_level.append(current_nesting_level)
    return max_nesting_level
