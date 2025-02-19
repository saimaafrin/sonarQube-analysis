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


    # Your code here
    # begin
    result = ''
    for i in range(len(s)):
        if s[i] not in c:
            result = result + s[i]
    for i in range(len(result)//2):
        if result[i] != result[-i-1]:
            return (result, False)
    return (result, True)
    # end
