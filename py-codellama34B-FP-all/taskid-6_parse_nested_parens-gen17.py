from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def find_deepest_level(input_string: str, current_level: int) -> int:
        """ Helper function to recursively find the deepest level of nesting for a string. """
        if '(' not in input_string:
            return current_level
        deepest_level = find_deepest_level(input_string[input_string.index('(')+1:], current_level+1)
        return max(deepest_level, current_level)

    return [find_deepest_level(group, 0) for group in paren_string.split(' ')]
