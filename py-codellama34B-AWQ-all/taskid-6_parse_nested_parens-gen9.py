from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    groups = paren_string.split(' ')
    #print('groups:', groups)
    result = []
    for g in groups:
        level = 1
        curr_max = 1
        in_parens = False
        for c in g:
            if c == '(':
                in_parens = True
                level += 1
                if level > curr_max:
                    curr_max = level
            elif c == ')':
                in_parens = False
                level -= 1
            else:
                raise Exception("Not a valid paren string")
        result.append(curr_max)
    return result
