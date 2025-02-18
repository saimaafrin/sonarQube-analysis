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

    str_list = list(s)
    res = ''
    for i in range(len(str_list)):
        if str_list[i].isalpha():
            res += str_list[i].swapcase()
        else:
            res += str_list[i]
    if len(res) == 0:
        return s[::-1]
    return res
