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

    if not s: return s
    return ''.join(chr(x ^ 32) if x >= 97 and x <= 122 else chr(x) if x >= 65 and x <= 90 else chr(x) for x in [ord(i) for i in s])
