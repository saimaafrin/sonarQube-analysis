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


    lst = list(map(lambda x: list(x), lst))

    open_parens = ['(']
    closed_parens = [')']

    for paren_list in lst:
        for paren in paren_list:
            if paren in open_parens:
                pass
            elif paren in closed_parens:
                pass
            else:
                raise ValueError(f'Unknown paren: {paren}')

    return 'Yes' if True else 'No'
