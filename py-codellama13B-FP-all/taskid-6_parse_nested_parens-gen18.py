from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    level = 0
    max_level = 0
    max_levels = []

    for c in paren_string:
        if c == '(':
            level += 1
            if level > max_level:
                max_level = level
        elif c == ')':
            level -= 1
    
    max_levels.append(max_level)

    return max_levels
