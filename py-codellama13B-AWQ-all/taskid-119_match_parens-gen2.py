from typing import List

def match_parens(lst: List[str]) -> str:
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    >>> match_parens(['()(', ')'])
    'Yes'
    >>> match_parens([')', ')'])
    'No'
    """

    # Initialization
    open_parens = '()'
    close_parens = '()'

    # Check if parens are balanced
    def check_parens(string):
        stack = []
        for char in string:
            if char in open_parens:
                stack.append(char)
            elif char in close_parens:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != open_parens[close_parens.index(char)]:
                    return False
        return len(stack) == 0

    # Check if concatenation is possible
    if len(lst[0]) == len(lst[1]) and check_parens(lst[0]) and check_parens(lst[1]):
        return 'Yes'
    else:
        return 'No'
