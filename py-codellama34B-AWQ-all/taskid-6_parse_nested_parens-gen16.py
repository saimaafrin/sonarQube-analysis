from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    def helper(paren_string: str, current_count: int, max_count: int) -> int:
        if not paren_string:
            return max_count
        first_char = paren_string[0]
        if first_char == '(':
            return helper(paren_string[1:], current_count + 1, max(max_count, current_count))
        if first_char == ')':
            return helper(paren_string[1:], current_count - 1, max(max_count, current_count))
        return helper(paren_string[1:], current_count, max_count)
    return [helper(paren_string, 0, 0) for paren_string in paren_string.split()]
