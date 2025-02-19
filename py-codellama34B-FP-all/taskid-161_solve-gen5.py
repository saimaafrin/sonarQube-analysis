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

    new_s = ''
    for c in s:
        if c.isalpha():
            new_s += c.swapcase()
        else:
            new_s += c
    return new_s[::-1] if not any(c.isalpha() for c in s) else new_s
