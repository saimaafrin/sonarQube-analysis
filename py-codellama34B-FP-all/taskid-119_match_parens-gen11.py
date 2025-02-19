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


    # good_parens = ['()', '()', '()']
    # bad_parens = ['(', '()']
    # bad_parens2 = [')', '()']

    # return 'Yes'

    good_parens = ['()', '()', '()']
    bad_parens = ['(', '()']
    bad_parens2 = [')', '()']

    # return 'No'

    # def is_balanced(p: str) -> bool:
    #     # Your code here
    #     stack = []
    #     for char in p:
    #         if char == "(":
    #             stack.append(char)
    #         elif char == ")":
    #             if not stack:
    #                 return False
    #             stack.pop()
    #     return not stack

    # def is_balanced(p: str) -> bool:
    #     count = 0
    #     for char in p:
    #         if char == "(":
    #             count += 1
    #         elif char == ")":
    #             count -= 1
    #             if count < 0:
    #                 return False
    #     return count == 0

    # def is_balanced(p: str) -> bool:
    #     count = 0
    #     for char in p:
    #         if char == "(":
    #             count += 1
    #         elif char == ")":
    #             count -= 1
    #     return count == 0

    # def is_balanced(p: str) -> bool:
    #     count = 0
    #     for char in p:
    #         if char == "(":
    #             count += 1
    #         elif char == ")":
    #             count -= 1
    #             if count < 0:
    #                 return False
    #     return count == 0

    def is_balanced(p: str) -> bool:
        count = 0
        for char in p:
            if char == "(":
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False
        return count == 0

    # good_parens = ['()', '()', '()']
    # bad_parens = ['(', '()']
    # bad_parens2 = [')', '()']

    def combine(parens1: List[str], parens2: List[str]) -> str:
        for p1 in parens1:
            for p2 in parens2:
                if is_balanced(p1 + p2):
                    return 'Yes'
        return 'No'

    return combine(lst[0], lst[1])
