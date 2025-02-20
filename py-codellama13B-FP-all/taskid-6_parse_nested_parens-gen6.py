from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def _count_nested_parens(string: str) -> int:
        level = 0
        for ch in string:
            if ch == '(':
                level += 1
            elif ch == ')':
                level -= 1
        return level

    return [_count_nested_parens(string.strip()) for string in paren_string.split()]
