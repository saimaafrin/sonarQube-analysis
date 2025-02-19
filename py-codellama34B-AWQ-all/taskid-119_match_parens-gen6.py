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


    def match_one(parens: str) -> bool:
        open_count = 0
        for c in parens:
            if c == '(':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False
        return open_count == 0

    return 'Yes' if any(
        match_one(str1 + str2)
        for str1 in lst
        for str2 in lst
    ) else 'No'
