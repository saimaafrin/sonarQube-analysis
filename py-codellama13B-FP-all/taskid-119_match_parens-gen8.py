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

    parens = dict()
    for i, char in enumerate(lst[0]):
        parens[i] = char

    for i, char in enumerate(lst[1]):
        if parens[i] == open_parens and char == close_parens:
            continue

        if parens[i] == close_parens and char == open_parens:
            parens[i] = open_parens
            continue

        return 'No'

    return 'Yes'
