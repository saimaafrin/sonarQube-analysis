def solve(s: str) -> str:
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    >>> solve('1234')
    '4321'
    >>> solve('ab')
    'AB'
    >>> solve('#a@C')
    '#A@c'
    """

    return ''.join(chr(ord('a') + ord('A') - ord(ch)) if ch.isalpha() else chr(ord('A') + ord('a') - ord(ch)) if ch.islower() else ch for ch in s[::-1])
