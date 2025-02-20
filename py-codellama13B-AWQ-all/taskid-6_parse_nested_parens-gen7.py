from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # first count the number of unpaired opening parentheses
    unpaired_parens = 0
    deepest_nesting = 0
    for c in paren_string:
        if c == '(':
            unpaired_parens += 1
        elif c == ')':
            unpaired_parens -= 1
        if unpaired_parens > deepest_nesting:
            deepest_nesting = unpaired_parens
    # now iterate over the string again, using a second counter to keep track
    # of the number of unpaired opening parentheses
    unpaired_parens = 0
    result = []
    for c in paren_string:
        if c == '(':
            unpaired_parens += 1
        elif c == ')':
            unpaired_parens -= 1
        if c == ' ':
            result.append(unpaired_parens)
            unpaired_parens = 0
    return result
