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

    s1 = lst[0]
    s2 = lst[1]
    bal = 0

    for i in range(len(s1)):
        if s1[i] == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            break

    for i in range(len(s2)):
        if s2[i] == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            break

    return 'Yes' if bal == 0 else 'No'
