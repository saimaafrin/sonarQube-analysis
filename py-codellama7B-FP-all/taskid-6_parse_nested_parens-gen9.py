from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    depth = 0
    result = []
    for char in paren_string:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if depth < 0:
            raise ValueError(f'Mismatched parenthesis {char} at {paren_string.index(char)}')
        if depth == 0:
            result.append(len(result) + 1)
    if depth != 0:
        raise ValueError('Mismatched parenthesis')
    return result
