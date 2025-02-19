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

    left_parens = 0

    for parens in lst[0]:
        if parens == "(":
            left_parens += 1
        else:
            left_parens -= 1
            if left_parens < 0:
                return "No"

    if left_parens == 0:
        return "Yes"

    right_parens = 0

    for parens in lst[1]:
        if parens == ")":
            right_parens += 1
        else:
            right_parens -= 1
            if right_parens < 0:
                return "No"

    if right_parens == left_parens:
        return "Yes"

    return "No"
