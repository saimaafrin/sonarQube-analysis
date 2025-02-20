from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    groups = paren_string.split(' ')
    nesting = [0]*len(groups)
    for i, group in enumerate(groups):
        count = 0
        for paren in group:
            if paren == '(':
                count += 1
            elif paren == ')':
                count -= 1
        nesting[i] = count
    return nesting
