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

    # Your code here
    # Left and right parentheses to close for each string.
    l_s1, r_s1, l_s2, r_s2 = 0, 0, 0, 0

    # Count the number of left and right parentheses in each string.
    for s in lst:
        for paren in s:
            if paren == "(":
                l_s1 += 1
            elif paren == ")":
                r_s1 += 1

    for s in lst:
        for paren in s:
            if paren == "(":
                l_s2 += 1
            elif paren == ")":
                r_s2 += 1

    # If the number of left and right parentheses are equal for each string.
    if l_s1 == r_s1 and l_s2 == r_s2:
        return "Yes"
    else:
        return "No"
