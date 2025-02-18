from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nest_levels = []
    max_nest_level = 0
    paren_string = paren_string.replace("(", " ( ").replace(")", " ) ")
    for paren in paren_string.split():
        if paren == "(":
            max_nest_level += 1
            nest_levels.append(max_nest_level)
        elif paren == ")":
            max_nest_level -= 1
    return nest_levels
