from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    split_string = paren_string.split(' ')
    output = []
    for string in split_string:
        level = 0
        current_level = 0
        for char in string:
            if char == '(':
                level += 1
                current_level = max(level, current_level)
            elif char == ')':
                level -= 1
        output.append(current_level)
    return output
