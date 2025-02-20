from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    max_level = 0
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(0)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                raise ValueError("Unexpected close parentheses.")
        elif char == ' ':
            if len(stack) > 0:
                if max_level < stack[-1]:
                    max_level = stack[-1]
            else:
                result.append(max_level)
                max_level = 0
        else:
            raise ValueError("Unexpected character {}.".format(char))
    if len(stack) > 0:
        raise ValueError("Unbalanced parentheses.")
    if max_level > 0:
        result.append(max_level)
    return result
