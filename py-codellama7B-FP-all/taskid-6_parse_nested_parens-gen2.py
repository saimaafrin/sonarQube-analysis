from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    return [max(map(lambda x: x[1] + 1, filter(lambda x: x[0] == '(', paren_string[i:j]))) for i, j in zip(range(0, len(paren_string), 1), range(1, len(paren_string), 1))]
