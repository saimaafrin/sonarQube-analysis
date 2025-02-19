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
        count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def concat(s1: str, s2: str) -> str:
        return s1 + s2

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_balanced(concat(lst[i], lst[j])):
                return 'Yes'
            if is_balanced(concat(lst[j], lst[i])):
                return 'Yes'
    return 'No'
