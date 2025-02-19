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

    s_list = list(s)
    for i, c in enumerate(s_list):
        if c.isalpha():
            if c.isupper():
                s_list[i] = c.lower()
            elif c.islower():
                s_list[i] = c.upper()
    if not any(c.isalpha() for c in s_list):
        return s[::-1]
    return "".join(s_list)
