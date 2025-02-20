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

    s0 = s0.lower()
    s1 = s1.lower()
    d0 = {}
    d1 = {}
    for c in s0:
        if c not in d0:
            d0[c] = 1
        else:
            d0[c] += 1

    for c in s1:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c] += 1

    return d0 == d1
