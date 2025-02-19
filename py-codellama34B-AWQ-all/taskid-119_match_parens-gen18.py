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

    if len(lst) != 2:
        raise ValueError('Length of lst must be 2')
    l1, l2 = lst
    if len(l1) + len(l2) % 2 == 1:
        return 'No'
    for p in ['(', ')']:
        if l1.count(p) + l2.count(p) % 2 == 1:
            return 'No'
    return 'Yes'
