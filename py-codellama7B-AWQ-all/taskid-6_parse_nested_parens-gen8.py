from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # First, we split by spaces to get groups of parentheses, then by parentheses to get individual nested parentheses.
    # After that, we count the number of parentheses to determine the depth
    return [len(group) for group in paren_string.split() for _ in group.split('()')]
