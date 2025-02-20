from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()
    nested_levels: List[int] = []
    for group in paren_string.split(' '):
        stack: List[str] = []
        level: int = 0
        for char in group:
            if char == '(':
                stack.append(char)
                level += 1
            else:
                stack.pop()
                if len(stack) > level:
                    level = len(stack)
        nested_levels.append(level)
    return nested_levels
