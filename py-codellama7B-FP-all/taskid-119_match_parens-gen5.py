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

    opening = ['(', '[', '{']
    closing = [')', ']', '}']

    def is_good(s: str) -> bool:
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if closing[opening.index(last)] != c:
                    return False
        return len(stack) == 0

    for i in range(2):
        if is_good(lst[i]):
            continue
        return 'No'
    return 'Yes'
