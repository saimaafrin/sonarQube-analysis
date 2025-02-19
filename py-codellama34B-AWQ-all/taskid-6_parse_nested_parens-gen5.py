from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def parse(s):
        level = 0
        for c in s:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
        return level

    return [parse(s) for s in paren_string.split(' ')]
