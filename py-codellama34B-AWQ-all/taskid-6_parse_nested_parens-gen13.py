from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.replace(' ', '')
    output = []

    for group in paren_string.split(')'):
        if group == '':
            continue
        else:
            group += ')'

        stack = []
        max_level = 0
        for c in group:
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
                if len(stack) > max_level:
                    max_level = len(stack)

        output.append(max_level)

    return output
