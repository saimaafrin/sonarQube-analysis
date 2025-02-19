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

    s1 = s2 = ""
    for char in lst[0]:
        if char == '(':
            s1 += '('
        else:
            if s1:
                s1 = s1[:-1]
            else:
                s1 += ')'
    if s1:
        return 'No'
    for char in lst[1]:
        if char == '(':
            s2 += '('
        else:
            if s2:
                s2 = s2[:-1]
            else:
                s2 += ')'
    if s2:
        return 'No'
    return 'Yes'
