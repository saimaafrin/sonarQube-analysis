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

    def helper(char: str) -> str:
        if char.islower():
            return char.upper()
        elif char.isupper():
            return char.lower()
        else:
            return char

    def isLetter(char: str) -> bool:
        return char.isalpha()

    def isLetter2(char: str) -> bool:
        return char.isalnum()

    return "".join(map(helper, list(map(lambda x: x if not isLetter(x) else x, list(s)))))
