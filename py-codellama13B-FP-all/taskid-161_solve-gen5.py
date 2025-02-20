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

    s = [i for i in s]
    for i, el in enumerate(s):
        if el.isalpha():
            s[i] = el.upper() if el.islower() else el.lower()
    if not s[0].isalpha():
        return s[::-1]
    return ''.join(s)
