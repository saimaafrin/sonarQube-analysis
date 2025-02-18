from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    # Split the input into each group of nested parentheses
    groups = paren_string.split()
    results = []

    for group in groups:
        # Keep track of how many opening and closing parens we have
        open_parens = 0
        close_parens = 0

        for char in group:
            # Keep track of how many opening and closing parens we have
            if char == '(':
                open_parens += 1
            elif char == ')':
                close_parens += 1

            # If we have the same number of opening and closing parens, then we have a maximum
            # level of nesting for this group
            if open_parens == close_parens:
                results.append(open_parens)
                break

        # If we don't have the same number of opening and closing parens, then we keep track of
        # the number of opening parens to know the maximum level of nesting for this group
        else:
            results.append(open_parens)

    return results
