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

    left_count = 0
    right_count = 0
    for p in lst[0]:
        if p == '(':
            left_count += 1
        else:
            left_count -= 1
            if left_count < 0:
                return 'No'
    for p in lst[1]:
        if p == ')':
            right_count += 1
        else:
            right_count -= 1
            if right_count < 0:
                return 'No'

    return 'Yes' if left_count == right_count else 'No'
