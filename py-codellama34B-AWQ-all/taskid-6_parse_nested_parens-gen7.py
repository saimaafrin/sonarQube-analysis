from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    group_list = paren_string.split(" ")
    paren_levels = []

    for group in group_list:
        curr_paren_level = 0
        stack = []
        for paren in group:
            if paren == "(":
                stack.append(paren)
                curr_paren_level += 1
            else:
                stack.pop()

            if len(stack) == 0:
                curr_paren_level = 0

            if len(stack) > curr_paren_level:
                curr_paren_level = len(stack)

        paren_levels.append(curr_paren_level)

    return paren_levels
