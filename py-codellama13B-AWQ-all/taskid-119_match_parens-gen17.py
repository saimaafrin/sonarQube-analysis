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

    # check if the strings are the same length
    # if not, it will not be possible to balance the parentheses
    if len(lst[0]) != len(lst[1]):
        return 'No'

    # initialize a variable to keep track of the number of open parentheses
    # if this number is never 0, then the parentheses are not balanced
    # therefore, it is not possible to make a good string
    open_parens = 0

    # iterate through both strings, and check if the parentheses are balanced
    # if they are not, it is not possible to make a good string
    # if they are, then return 'Yes'
    for i in range(len(lst[0])):
        if lst[0][i] == '(':
            open_parens += 1
        else:
            open_parens -= 1
        if open_parens < 0:
            return 'No'
    for i in range(len(lst[1])):
        if lst[1][i] == '(':
            open_parens += 1
        else:
            open_parens -= 1
        if open_parens < 0:
            return 'No'
    if open_parens == 0:
        return 'Yes'
    else:
        return 'No'
