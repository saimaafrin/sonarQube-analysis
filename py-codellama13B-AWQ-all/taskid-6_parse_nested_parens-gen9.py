from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def find_max_depth_of_nesting(paren_string: str) -> int:
        """ Find the maximum depth of nesting of parentheses.
        """
        level = 0
        for char in paren_string:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
        return level

    results = []
    for paren_group in paren_string.split():
        results.append(find_max_depth_of_nesting(paren_group))
    return results
