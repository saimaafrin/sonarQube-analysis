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

    # open_list = ['(']
    # close_list = [')']
    # if (')' in lst[1] and '(' in lst[0]):
    #     return 'Yes'
    # elif (')' in lst[0] and '(' in lst[1]):
    #     return 'Yes'
    # else:
    #     return 'No'
    # return ''.join(lst)

    # stack = []
    # for i in lst[0]:
    #     if i == '(':
    #         stack.append('(')
    #     else:
    #         if len(stack) > 0:
    #             stack.pop()
    #         else:
    #             return 'No'
    # for i in lst[1]:
    #     if i == ')':
    #         if len(stack) > 0:
    #             stack.pop()
    #         else:
    #             return 'No'
    #     else:
    #         stack.append('(')

    # return 'Yes' if len(stack) == 0 else 'No'
    # s = ''.join(lst)
    # print(s)
    # stack = []
    # for i in range(len(s)):
    #     if s[i] == '(':
    #         stack.append('(')
    #     else:
    #         if len(stack) > 0:
    #             stack.pop()
    #         else:
    #             return 'No'
    # print(stack)
    # return 'Yes' if len(stack) == 0 else 'No'
    s = ''.join(lst)
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return 'No'
    return 'Yes' if len(stack) == 0 else 'No'
