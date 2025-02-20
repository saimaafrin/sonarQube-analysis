from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # The output list
    max_depth_list = []

    # List of nested parentheses
    nested_parens_list = paren_string.split(' ')

    for nested_parens in nested_parens_list:
        # Initialize current depth
        current_depth = 0

        # Loop through all parentheses in the nested parentheses
        for paren in nested_parens:
            # If opening parentheses, increment the depth
            if paren == '(':
                current_depth += 1
            # If closing parentheses, decrement the depth
            elif paren == ')':
                current_depth -= 1

        # Add the maximum depth of the current group to the output list
        max_depth_list.append(current_depth)

    return max_depth_list
