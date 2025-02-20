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

    # First solution
    # s = list(s)
    # c = list(c)
    # for i in range(len(c)):
    #     s = [j for j in s if c[i] != j]
    # for i in range(len(s)):
    #     if s[i] != s[len(s)-i-1]:
    #         return ("".join(s), False)
    # return ("".join(s), True)

    # Second solution
    # s = s.replace(c, '')
    # for i in range(len(s)):
    #     if s[i] != s[len(s)-i-1]:
    #         return (s, False)
    # return (s, True)

    # Third solution
    # s = list(s)
    # c = list(c)
    # for i in range(len(c)):
    #     s = [j for j in s if c[i] != j]
    # while s[0] == s[len(s)-1]:
    #     s.pop(0)
    #     s.pop()
    # if len(s) == 0:
    #     return ("", True)
    # return ("".join(s), False)

    # Fourth solution
    # s = list(s)
    # c = list(c)
    # for i in range(len(c)):
    #     s = [j for j in s if c[i] != j]
    # while s[0] == s[len(s)-1]:
    #     s.pop(0)
    #     s.pop()
    # return ("".join(s), len(s) == 0)

    # Fifth solution
    # s = s.replace(c, '')
    # while s[0] == s[len(s)-1]:
    #     s = s[1:-1]
    # return (s, len(s) == 0)

    # Sixth solution
    s = s.replace(c, '')
    return (s, s[::-1] == s)
