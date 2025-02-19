from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()
    parenthesis_list = paren_string.split()

    max_levels: List[int] = []
    for parens in parenthesis_list:
        level = 0
        for char in parens:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
            if level < 0:
                raise ValueError(f'Incorrect format of parenthesis: {parens}')
        max_levels.append(level)
    return max_levels
