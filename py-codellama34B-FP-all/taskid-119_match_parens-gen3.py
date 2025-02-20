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

    # Your code here

    # 1. Find the first right parentheses, and move it to the end of the list.
    # 2. If you moved a right parentheses to the end of the list, find the next right parentheses and move it.
    # 3. If you reached the end of the list without finding any right parentheses, the string is good.
    # 4. If you reached the end of the list without finding any left parentheses, the string is not good.
    # 5. If there are no parentheses, the string is good.
    # 6. If there is only one parentheses, the string is not good.

    # Check if the string is good
    def is_good(s: str) -> bool:
        stack = 0
        for i in s:
            if i == '(':
                stack += 1
            else:
                stack -= 1
            if stack < 0:
                return False
        if stack > 0:
            return False
        return True

    # Move the right parentheses to the end of the list
    def move_right(lst: List[str]) -> List[str]:
        for i in range(len(lst)):
            if lst[i] == ')':
                lst.append(lst.pop(i))
                break
        return lst

    # If there are only left parentheses, the string is not good
    if all(e == '(' for e in lst[0] + lst[1]):
        return 'No'

    # If there are no parentheses, the string is good
    if len(lst[0] + lst[1]) == 0:
        return 'Yes'

    # If there is only one parentheses, the string is not good
    if len(lst[0] + lst[1]) == 1:
        return 'No'

    # If there are more than two left parentheses, the string is not good
    if lst[0].count('(') > 2 or lst[1].count('(') > 2:
        return 'No'

    # If there are more than two right parentheses, the string is not good
    if lst[0].count(')') > 2 or lst[1].count(')') > 2:
        return 'No'

    # Check if the string is good
    if is_good(lst[0] + lst[1]):
        return 'Yes'

    # Move the right parentheses to the end of the list
    lst = move_right(lst)

    # Check if the string is good
    if is_good(lst[0] + lst[1]):
        return 'Yes'

    # If the string is not good, return No
    return 'No'
