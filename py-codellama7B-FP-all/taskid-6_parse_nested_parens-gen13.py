from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    depth_list = [0]
    for paren_level in paren_string.split():
        depth = 0
        for char in paren_level:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
        if depth_list[-1] < depth:
            depth_list.append(depth)
        else:
            depth_list.append(depth_list[-1])
    return [depth_list[i] for i in range(len(depth_list)) if depth_list[i] != depth_list[i-1]]
