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

    if not c:
        return s, True

    s_list = list(s)
    c_list = list(c)
    for i in range(len(s_list)):
        if s_list[i] in c_list:
            s_list.pop(i)
            i -= 1

    s = ''.join(s_list)
    return s, s == s[::-1]
