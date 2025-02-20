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

    s1, s2 = lst
    s1 = list(s1)
    s2 = list(s2)
    while len(s1) != 0 and len(s2) != 0:
        if s1[-1] == '(' and s2[-1] == ')':
            s1.pop()
            s2.pop()
        elif s1[-1] == ')' and s2[-1] == '(':
            s1.pop()
            s2.pop()
        elif s1[-1] == '(':
            s1.pop()
        elif s2[-1] == ')':
            s2.pop()
        else:
            return 'No'
    return 'Yes'
