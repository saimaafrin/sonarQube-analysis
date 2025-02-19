def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    d = {}
    for c in s0:
        d[c] = d.get(c, 0) + 1
    for c in s1:
        if c not in d or d[c] <= 0:
            return False
        d[c] -= 1
    for _, v in d.items():
        if v != 0:
            return False
    return True
