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

    if len(lst) == 1:
        return "Yes" if not lst[0] else "No"
    if len(lst) == 2:
        if lst[0] == "(" and lst[1] == ")":
            return "Yes"
        elif lst[0] == ")" and lst[1] == "(":
            return "Yes"
        else:
            return "No"
    if len(lst) > 2:
        if len(lst) % 2 != 0:
            return "No"
        i = 0
        for paren in lst:
            if paren == "(":
                i += 1
            else:
                i -= 1
        return "Yes" if i == 0 else "No"
    return "No"
