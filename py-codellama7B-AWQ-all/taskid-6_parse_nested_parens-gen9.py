from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # List of strings with each string representing a group
    str_list = paren_string.split(' ')

    # List of lists containing the depths of the nesting
    # For example, in the input string (()()) ((())) () ((())()())
    # the list will be [[2, 1], [3, 1], [1], [3, 2]]
    depth_list = [get_nested_depth(str_list[i]) for i in range(len(str_list))]

    return [max(depth) for depth in depth_list]
