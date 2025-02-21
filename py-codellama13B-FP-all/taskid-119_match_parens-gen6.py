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

    open_count = 0
    close_count = 0
    for paren in lst:
        if paren == '(':
            open_count += 1
        else:
            close_count += 1
        if close_count > open_count:
            return 'No'
    if open_count == close_count:
        return 'Yes'
    if close_count > open_count:
        return 'No'
    if open_count > close_count:
        return 'No'
