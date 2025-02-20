from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if not paren_string:
        return []

    groups = paren_string.split()
    result = []
    for g in groups:
        level = 0
        current_level = 0
        for ch in g:
            if ch == '(':
                current_level += 1
                level = max(level, current_level)
            elif ch == ')':
                current_level -= 1
                assert current_level >= 0
            else:
                raise Exception('Invalid character')
        assert current_level == 0
        result.append(level)
    return result
