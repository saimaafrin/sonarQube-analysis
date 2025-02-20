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


    def is_good(string: str) -> bool:
        # A string is good if all parentheses in S are balanced.
        # We can check that by using a stack.
        stack = []

        for char in string:
            if char == '(':
                stack.append(char)
            else:
                if len(stack) == 0:
                    # If the stack is empty, then we can't balance the
                    # parentheses.
                    return False

                stack.pop()

        return len(stack) == 0

    return 'Yes' if is_good(lst[0]) and is_good(lst[1]) else 'No'
