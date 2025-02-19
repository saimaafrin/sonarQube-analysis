from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    assert paren_string.startswith('(') and paren_string.endswith(')') and len(paren_string) > 2, 'Invalid input string'
    paren_groups = paren_string.strip('()').split(' ')
    # print('paren_groups: ', paren_groups)
    paren_levels = []
    for group in paren_groups:
        paren_levels.append(group_nesting_level(group))

    return paren_levels
