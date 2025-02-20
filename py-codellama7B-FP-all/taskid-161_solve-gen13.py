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

    result = []
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()
        else:
            s[i] = s[i]
    result = ''.join(s)
    return result
