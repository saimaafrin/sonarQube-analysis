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

    # Your code here
    lower = 0
    upper = 0
    l = []
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                l.append(s[i].upper())
                upper += 1
            else:
                l.append(s[i].lower())
                lower += 1
        else:
            l.append(s[i])
    if upper == 0:
        return ''.join(l[::-1])
    else:
        return ''.join(l)
