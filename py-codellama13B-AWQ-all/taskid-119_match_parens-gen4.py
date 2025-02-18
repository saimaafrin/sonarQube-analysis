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

    result = 'No'
    if '(' in lst[0] and ')' in lst[1]:
        if len(lst[0]) == len(lst[1]):
            result = 'Yes'
    elif ')' in lst[0] and '(' in lst[1]:
        if len(lst[0]) == len(lst[1]):
            result = 'Yes'
    return result
