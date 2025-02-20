from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.replace("(", "")
    paren_string = paren_string.replace(")", "")
    stack: List[int] = []
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append(i)
        elif c == ')':
            stack.pop()
            if len(stack) > 0:
                stack[-1] += 1
            else:
                stack.append(1)
    return stack
