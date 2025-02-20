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

    if not s:
        return s
    res = []
    for i, c in enumerate(s):
        if c.isalpha():
            res.append(c.swapcase())
        else:
            res.append(c)
    return ''.join(res)
