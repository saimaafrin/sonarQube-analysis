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

    def check_brackets(string: str) -> bool:
        """
        Checks if the bracket is balanced.
        """
        brackets = []
        for char in string:
            if char == '(':
                brackets.append(char)
            else:
                if len(brackets) == 0:
                    return False
                brackets.pop()
        return len(brackets) == 0

    string1 = lst[0]
    string2 = lst[1]

    result = string1 + string2
    return 'Yes' if check_brackets(result) else 'No'
