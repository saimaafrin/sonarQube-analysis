from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_strings = paren_string.split(' ')
    result = []
    for paren_string in paren_strings:
        level = 0
        max_level = 0
        for paren in paren_string:
            if paren == '(':
                level += 1
            else:
                level -= 1
            max_level = max(max_level, level)
        result.append(max_level)
    return result
