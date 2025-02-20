from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []

    # Remove all the spaces, and split based on '(' and ')'
    splitted = paren_string.replace(' ', '').split('(')

    # Remove the empty string at the beginning
    splitted.pop(0)

    # Iterate through each paren group
    for group in splitted:
        # Count how many '(' and ')' are present
        count = 0
        for char in group:
            if char == '(':
                count += 1
            else:
                count -= 1

        # Add the maximum number of nesting to the result
        result.append(count)

    return result
