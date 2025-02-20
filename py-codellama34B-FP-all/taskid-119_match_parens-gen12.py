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

    open_parens = '('
    close_parens = ')'
    parens = []
    for i in range(len(lst[0])+len(lst[1])):
        if i < len(lst[0]):
            if lst[0][i] == open_parens:
                parens.append(open_parens)
            else:
                parens.pop()
        if i < len(lst[1]):
            if lst[1][i] == open_parens:
                parens.append(open_parens)
            else:
                parens.pop()
    if parens:
        return 'No'
    return 'Yes'
