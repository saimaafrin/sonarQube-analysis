from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_level_nesting = []
    nesting_level = 0
    for ch in paren_string:
        if ch == '(':
            nesting_level += 1
        elif ch == ')':
            nesting_level -= 1
        if nesting_level > max_level_nesting[-1] if len(max_level_nesting) != 0 else 0:
            max_level_nesting.append(nesting_level)
    return max_level_nesting
