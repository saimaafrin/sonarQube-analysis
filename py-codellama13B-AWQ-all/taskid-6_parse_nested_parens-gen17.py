from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # create a list of tuples of each nested group
    # and their starting and ending indices
    nested_groups = [(m.start(), m.end()) for m in re.finditer(r'\((.*?)\)', paren_string)]

    # create a list of tuples for each nested group of the
    # starting and ending indices of the innermost parentheses
    innermost_parens = [(m.start() + 1, m.end() - 1) for m in re.finditer(r'\((.*?)\)', paren_string)]

    # return a list of the difference between the starting and ending indices
    # of each innermost parentheses
    return [m[1] - m[0] for m in innermost_parens]
