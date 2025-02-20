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

    strlist = list(s)
    for i in range(len(strlist)):
        if strlist[i].isalpha():
            if strlist[i].islower():
                strlist[i] = strlist[i].upper()
            else:
                strlist[i] = strlist[i].lower()
    if not any(c.isalpha() for c in strlist):
        strlist = strlist[::-1]
    return ''.join(strlist)
