from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Initialize the list that will contain the output
    out = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Go through each group and count the number of levels of nesting
    for group in groups:
        # Initialize the count of levels of nesting
        count = 0

        # Iterate through the characters of the group
        for char in group:
            # If a left parenthesis is encountered, increment the count
            if char == '(':
                count += 1
            # If a right parenthesis is encountered, decrement the count
            elif char == ')':
                count -= 1

        # Add the count to the list of outputs
        out.append(count)

    return out
