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


    # Initialize the variables
    i = 0
    j = 0
    count = 0

    # Iterate through both the strings
    for i in range(len(lst[0])):
        for j in range(len(lst[1])):
            # If there's a match, increment the count variable
            if lst[0][i] == lst[1][j]:
                count += 1
            # If there's no match, return 'No'
            else:
                return 'No'

    # If the count variable is even, return 'Yes'
    if count % 2 == 0:
        return 'Yes'
    # If the count variable is odd, return 'No'
    else:
        return 'No'
