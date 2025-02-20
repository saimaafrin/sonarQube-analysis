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

    def match_parens_helper(l1, l2):
        open_list = []
        for paren in l1:
            if paren == ')':
                if open_list:
                    open_list.pop()
                else:
                    open_list.append(paren)
            else:
                open_list.append(paren)
        for paren in l2:
            if paren == ')':
                if open_list:
                    open_list.pop()
                else:
                    open_list.append(paren)
            else:
                open_list.append(paren)

        return open_list == []

    return 'Yes' if match_parens_helper(lst[0], lst[1]) else 'No'
