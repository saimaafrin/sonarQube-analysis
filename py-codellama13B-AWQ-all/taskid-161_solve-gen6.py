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

    is_num = True
    for char in s:
        if char.isalpha():
            is_num = False
            break

    if is_num:
        return s[::-1]
    else:
        res = ''
        for char in s:
            if char.isalpha():
                if char.islower():
                    res += char.upper()
                else:
                    res += char.lower()
            else:
                res += char

    return res
