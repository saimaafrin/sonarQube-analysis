from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    >>> reverse_delete('abcde', 'ae')
    ('bcd', False)
    >>> reverse_delete('abcdef', 'b')
    ('acdef', False)
    >>> reverse_delete('abcdedcba', 'ab')
    ('cdedc', True)
    """

    s = list(s)
    c = list(c)
    result = []
    for i in s:
        if i not in c:
            result.append(i)
    if ''.join(result)[::-1] == ''.join(result):
        return ''.join(result), True
    else:
        return ''.join(result), False
