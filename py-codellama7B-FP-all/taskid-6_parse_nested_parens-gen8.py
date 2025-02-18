from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    level = 0
    level_stack = []
    max_level = 0

    for char in paren_string:
        if char == '(':
            level += 1
            level_stack.append(char)
        elif char == ')':
            level -= 1
            if level == 0:
                max_level = max(max_level, len(level_stack))
                level_stack = []
        else:
            assert False, f'Unknown char: {char}'
    return [level]

    # This works too:
    # def parse_nested_parens(paren_string: str) -> List[int]:
    #     """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    #     For each of the group, output the deepest level of nesting of parentheses.
    #     E.g. (()()) has maximum two levels of nesting while ((())) has three.

    #     >>> parse_nested_parens('(()()) ((())) () ((())()())')
    #     [2, 3, 1, 3]
    #     """
    #     level_stack = []
    #     max_level = 0

    #     for char in paren_string:
    #         if char == '(':
    #             level_stack.append(char)
    #         elif char == ')':
    #             level_stack.pop()
    #         else:
    #             assert False, f'Unknown char: {char}'
    #     return [len(level_stack)]

    # This doesn't work. It is a naive solution that doesn't take into account the spaces:
    # def parse_nested_parens(paren_string: str) -> List[int]:
    #     """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    #     For each of the group, output the deepest level of nesting of parentheses.
    #     E.g. (()()) has maximum two levels of nesting while ((())) has three.

    #     >>> parse_nested_parens('(()()) ((())) () ((())()())')
    #     [2, 3, 1, 3]
    #     """
    #     return [len(list(filter(lambda x: x == '(', paren_string)))]

    # This is another naive solution that doesn't take into account the spaces:
    # def parse_nested_parens(paren_string: str) -> List[int]:
    #     """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    #     For each of the group, output the deepest level of nesting of parentheses.
    #     E.g. (()()) has maximum two levels of nesting while ((())) has three.

    #     >>> parse_nested_parens('(()()) ((())) () ((())()())')
    #     [2, 3, 1, 3]
    #     """
    #     count = 0
    #     max_level = 0
    #     for char in paren_string:
    #         if char == '(':
    #             count += 1
    #         elif char == ')':
    #             count -= 1
    #             if count == 0:
    #                 max_level = max(max_level, count)
    #         else:
    #             assert False, f'Unknown char: {char}'
    #     return [max_level]
