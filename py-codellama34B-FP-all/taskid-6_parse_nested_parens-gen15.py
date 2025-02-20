from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    groups = paren_string.split(' ')
    levels = [0] * len(groups)
    for i, g in enumerate(groups):
        levels[i] = max(levels[i - 1] - 1, 0)
        stack = []
        for c in g:
            if c == '(':
                stack.append(c)
                levels[i] = max(levels[i], len(stack))
            elif c == ')':
                stack.pop()
    return levels
