from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # You can get rid of the empty strings if you want
    parens_and_empty_str = paren_string.split()
    max_parens_nesting = []
    for parens in parens_and_empty_str:
        max_parens_nesting.append(max(parens.count(i) for i in ["(", ")"]))

    return max_parens_nesting
