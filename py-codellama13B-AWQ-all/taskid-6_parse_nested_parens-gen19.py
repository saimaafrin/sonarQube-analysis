from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    results = []
    for group in paren_string.split():
        cur_level = 0
        max_level = 0
        for char in group:
            if char == '(':
                cur_level += 1
                if cur_level > max_level:
                    max_level = cur_level
            elif char == ')':
                cur_level -= 1
        results.append(max_level)
    return results
