from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def helper(paren_string: str) -> int:
        stack = []
        for c in paren_string:
            if c == '(':
                stack.append(1)
            elif c == ')':
                stack.pop()
                stack[-1] += 1
        return stack[0] if stack else 0

    return [helper(group) for group in paren_string.split()]
