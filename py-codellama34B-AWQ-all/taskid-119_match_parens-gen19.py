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

    paren_stack = []

    for paren in lst[0]:
        if paren == '(':
            paren_stack.append(paren)
        else:
            if len(paren_stack) == 0:
                return 'No'
            paren_stack.pop()
    for paren in lst[1]:
        if paren == '(':
            paren_stack.append(paren)
        else:
            if len(paren_stack) == 0:
                return 'No'
            paren_stack.pop()

    return 'Yes' if len(paren_stack) == 0 else 'No'
