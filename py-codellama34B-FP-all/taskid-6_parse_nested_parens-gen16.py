from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def parse_one(paren_string: str) -> int:
        """ Takes one group of nested parentheses and returns the maximum level of nesting.

        >>> parse_one('()')
        1
        >>> parse_one('(((()())))')
        5
        >>> parse_one('((()()())(()()))')
        4
        >>> parse_one('((((()))))')
        4
        >>> parse_one('((())())')
        3
        """
        stack: List[int] = []
        max_count: int = 0
        count: int = 0
        for paren in paren_string:
            if paren == '(':
                stack.append(count)
                count = 0
            elif paren == ')':
                count = stack.pop() + 1
                max_count = max(max_count, count)
            else:
                raise Exception(f"Invalid character in the parentheses: '{paren}'")
        if len(stack) != 0:
            raise Exception(f"Unbalanced parentheses: '{paren_string}'")
        return max_count
    return [parse_one(s) for s in paren_string.split(' ')]
