from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    depth_list = []
    current_depth = 0
    max_depth = 0
    for char in paren_string:
        if char == '(':
            current_depth += 1
            max_depth = max(current_depth, max_depth)
        elif char == ')':
            current_depth -= 1
        elif char == ' ':
            depth_list.append(max_depth)
            max_depth = 0
            current_depth = 0
    return depth_list
