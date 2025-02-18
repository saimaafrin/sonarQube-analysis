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

    def is_balanced(s: str) -> bool:
        """
        Checks if the number of open parens is equal to the number of closed ones
        in a given string.
        """
        parens = 0
        for c in s:
            if c == '(':
                parens += 1
            else:
                parens -= 1
            if parens < 0:
                return False
        return parens == 0

    s = ''.join(lst)
    return 'Yes' if is_balanced(s) else 'No'
