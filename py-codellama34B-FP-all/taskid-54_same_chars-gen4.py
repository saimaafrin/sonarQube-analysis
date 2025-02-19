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

    d0 = {}
    d1 = {}
    for c in s0:
        d0[c] = d0.get(c, 0) + 1
    for c in s1:
        d1[c] = d1.get(c, 0) + 1
    return d0 == d1
