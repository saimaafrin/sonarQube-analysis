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

    if not s:
        return s, False
    if not c:
        return s, s == s[::-1]

    result = ''
    i = 0
    while i < len(s):
        c1 = s[i]
        if c1 not in c:
            result += c1
        i += 1
    return result, result == result[::-1]
