from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    groups = paren_string.split()
    nested_parens = []

    for group in groups:
        count = 0
        max_level = 0
        for paren in group:
            if paren == '(':
                count += 1
            elif paren == ')':
                count -= 1
            if count > max_level:
                max_level = count
        nested_parens.append(max_level)

    return nested_parens
