from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_depths = []
    parens_stack = []
    for char in paren_string:
        if char == '(':
            parens_stack.append(char)
        elif char == ')':
            if not parens_stack:
                raise ValueError("Invalid parenthesis structure!")
            parens_stack.pop()
            if len(parens_stack) > 0:
                nested_depths.append(len(parens_stack))
    if parens_stack:
        raise ValueError("Invalid parenthesis structure!")
    return nested_depths
