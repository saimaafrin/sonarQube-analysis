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

    n = len(s)
    i, j = 0, 0
    while i < n and j < len(c):
        if s[i] == c[j]:
            i += 1
        else:
            s = s[:i] + s[i+1:]
        j += 1
    if i < n:
        s = s[:i] + s[i+1:]

    return s, s == s[::-1]
