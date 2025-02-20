from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Initialize output list.
    max_levels_of_nesting_list = []
    # Initialize starting nesting level for each group.
    current_nesting_level = 0
    for paren in paren_string.split(' '):
        # Update the current nesting level based on the number of open parens found.
        current_nesting_level += paren.count('(')
        # Add the maximum nesting level for this group to the output list.
        max_levels_of_nesting_list.append(current_nesting_level)
        # Update the current nesting level based on the number of close parens found.
        current_nesting_level -= paren.count(')')
    # Return the output list.
    return max_levels_of_nesting_list
