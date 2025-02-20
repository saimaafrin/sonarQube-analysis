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

    if len(s) == 0:
        return s
    letters = [ch for ch in s if ch.isalpha()]
    if len(letters) == 0:
        return s[::-1]
    else:
        return ''.join(ch.lower() if ch.isupper() else ch.upper() if ch.islower() else ch
                       for ch in s)
