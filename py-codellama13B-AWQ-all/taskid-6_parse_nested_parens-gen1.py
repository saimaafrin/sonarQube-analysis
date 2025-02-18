from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    level = 0
    deepest = 0
    output = []
    for char in paren_string:
        if char == '(':
            level += 1
            if level > deepest:
                deepest = level
        elif char == ')':
            level -= 1
        elif char == ' ':
            output.append(deepest)
            deepest = 0
        else:
            raise ValueError(f'Invalid character encountered: {char}')
    return output
