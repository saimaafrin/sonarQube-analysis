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

    stack = []
    for i in range(len(lst[0])):
        if lst[0][i] == "(":
            stack.append(lst[0][i])
        else:
            if len(stack) == 0:
                return "No"
            stack.pop()
    for i in range(len(lst[1])):
        if lst[1][i] == "(":
            stack.append(lst[1][i])
        else:
            if len(stack) == 0:
                return "No"
            stack.pop()
    if len(stack) == 0:
        return "Yes"
    else:
        return "No"
