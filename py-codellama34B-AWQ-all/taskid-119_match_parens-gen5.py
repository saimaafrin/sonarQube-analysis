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


    first_string = lst[0]
    second_string = lst[1]

    first_string_count = 0
    for i in first_string:
        if i == '(':
            first_string_count += 1
        else:
            first_string_count -= 1

    second_string_count = 0
    for i in second_string:
        if i == '(':
            second_string_count += 1
        else:
            second_string_count -= 1

    if first_string_count + second_string_count == 0:
        return 'Yes'
    else:
        return 'No'
