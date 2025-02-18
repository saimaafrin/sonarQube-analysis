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
    s1 = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                s1 += c.upper()
            else:
                s1 += c.lower()
        else:
            s1 += c
    return s1

    # Another Solutions
    return s.swapcase()
