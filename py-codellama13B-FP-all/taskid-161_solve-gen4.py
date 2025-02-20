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

    # 012345
    # abBA
    # [::-1]
    # 'abBA'[::-1]
    # 'BAb'[::-1]
    # 'BA'
    # 'aB'[::-1]
    # 'bA'
    return s[::-1] if s.isalnum() else ''.join(x.swapcase() if x.isalpha() else x for x in s)
