from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    deepest_level_of_nesting = 0
    answer_list = []
    for paren_group in paren_string.split():
        current_level_of_nesting = 0
        for paren in paren_group:
            if paren == '(':
                current_level_of_nesting += 1
            else:
                current_level_of_nesting -= 1
        if current_level_of_nesting > deepest_level_of_nesting:
            deepest_level_of_nesting = current_level_of_nesting
        answer_list.append(deepest_level_of_nesting)
    return answer_list
