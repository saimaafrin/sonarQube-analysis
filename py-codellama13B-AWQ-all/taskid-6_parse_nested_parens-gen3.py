from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_list = []
    deepest_level = 0
    deepest_level_temp = 0
    for nested_paren in paren_string.split(' '):
        for char in nested_paren:
            if char == '(':
                deepest_level_temp += 1
            elif char == ')':
                deepest_level_temp -= 1
        nested_list.append(deepest_level_temp)
        if deepest_level < deepest_level_temp:
            deepest_level = deepest_level_temp
        deepest_level_temp = 0
    return nested_list
