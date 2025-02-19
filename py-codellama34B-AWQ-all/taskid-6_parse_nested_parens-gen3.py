from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_level = 0
    stack = []
    current_level = 0
    output = []

    for char in paren_string:
        if char == "(":
            current_level += 1
            if current_level > max_level:
                max_level = current_level
            stack.append(char)
        elif char == ")":
            stack.pop()
            if not stack:
                current_level = 0
            else:
                current_level = len(stack)
        elif char == " ":
            output.append(max_level)
            max_level = current_level
    return output
