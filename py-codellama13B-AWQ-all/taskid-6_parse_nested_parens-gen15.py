from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    output = []
    paren_string = paren_string.strip()
    groups = paren_string.split(' ')
    for group in groups:
        level = 0
        for char in group:
            if char == '(':
                level += 1
            else:
                level -= 1
        output.append(level)
    return output
