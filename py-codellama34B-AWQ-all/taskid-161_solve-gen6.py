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
    is_letter = s.isalpha()
    if not is_letter:
        return s[::-1]
    return "".join(s[i].swapcase() if s[i].isalpha() else s[i] for i in range(len(s)))
