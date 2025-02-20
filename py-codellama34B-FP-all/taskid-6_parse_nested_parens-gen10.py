from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    levels = []
    for parens in paren_string.split():
        level = 0
        for i, char in enumerate(parens):
            if char == '(':
                level += 1
            elif char == ')':
                if level == 0:
                    raise ValueError(f'Mismatched parenthesis at index {i} in "{parens}"')
                else:
                    level -= 1
        levels.append(level)
    return levels
