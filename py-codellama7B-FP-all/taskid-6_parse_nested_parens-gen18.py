from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Initialize a list of integers for storing the level of nesting.
    level_list = []

    # Iterate through the string, and check if the character is an opening bracket
    # If it is, then add one to the level of nesting and store it to the list.
    for i in paren_string:
        if i == '(':
            level_list.append(level_list[-1] + 1)
        # If the character is a closing bracket, then subtract one from the level
        # of nesting and store it to the list.
        elif i == ')':
            level_list.append(level_list[-1] - 1)

    # After iterating through the entire string, the last element of the list
    # should be the level of nesting at the outermost scope.
    # Return the list.
    return level_list
